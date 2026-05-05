# /src/gui/streamlit/components/patient_flow_diagram.py

from pathlib import Path
from typing import Any, TypeAlias

from src.domain.mobile_app_types import (
    DataRead,
    DataWrite,
    NavigationRoute,
    ScreenSpec,
)
from src.gui.streamlit.utils.convert_png_to_text import image_to_data_uri

from src.infrastructure.renderer.flow_diagram.diagram_nodes.node_content_to_diagram_ui_adapter import (
    flow_node_to_node_info,
)

import json
import streamlit.components.v1 as components

STATIC_DIR = Path(__file__).resolve().parents[1] / "static"
# ASSETS_DIR = STATIC_DIR / "assets"
IMAGES_DIR = STATIC_DIR / "assets" / "images"
CSS_PATH = STATIC_DIR / "flow_diagram.css"
JS_PATH = STATIC_DIR / "flow_diagram.js"

PatientFlowNodeValue: TypeAlias = str | list[str]
PatientFlowNode: TypeAlias = dict[str, Any]
PatientFlowNodes: TypeAlias = dict[str, PatientFlowNode | ScreenSpec]


# backend = getattr(screen, "backend_data_model", None)


def _load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _get_embedded_html(config_json: str, js: str, css: str) -> str:
    return f"""
<!doctype html>
<html lang="en">

<head>
    <meta charset="UTF-8" />

    <script>
        window.patientFlowConfig = {config_json};
    </script>

    <script type="module">
        {js}
    </script>

    <style>
        {
    css
    }
    </style>
</head>

<body>
    <div class="chart-card">
        <div id="chart"></div>
    </div>

    <section id="node-details-frame" class="details-frame hidden">
        <h3 id="node-details-title"></h3>

        <details open>
            <summary>Screen Specification</summary>
        
            <h4>Purpose</h4>
            <p id="node-screen-spec"></p>
        
            <h4>Displayed Data</h4>
            <ul id="node-screen-displayed-data"></ul>
        
            <h4>User Inputs</h4>
            <ul id="node-screen-user-inputs"></ul>
        
            <h4>Primary Action</h4>
            <p id="node-screen-primary-action"></p>
        
            <h4>Secondary Actions</h4>
            <ul id="node-screen-secondary-actions"></ul>
        
            <h4>Validation Rules</h4>
            <ul id="node-screen-validation-rules"></ul>
        
            <h4>Navigation In</h4>
            <ul id="node-screen-navigation-in"></ul>
        
            <h4>Navigation Out</h4>
            <ul id="node-screen-navigation-out"></ul>
        
            <h4>States</h4>
            <p><strong>Empty:</strong> <span id="node-screen-empty-state"></span></p>
            <p><strong>Loading:</strong> <span id="node-screen-loading-state"></span></p>
            <p><strong>Error:</strong> <span id="node-screen-error-state"></span></p>
        </details>

        <details>
            <summary>Screen Sketches</summary>
            <div id="node-details-images" class="details-images"></div>
            <p id="node-details-image-empty" class="muted hidden">
                No screen sketches available.
            </p>
        </details>

        <!--
            
            <details>
                <summary>Primary Actions</summary>
                <ul id="node-primary-actions"></ul>
            </details>
    
            <details>
                <summary>User Roles</summary>
                <ul id="node-users"></ul>
            </details>
            
            -->

        <details>
            <summary>Use Cases</summary>
            <div id="node-use-cases"></div>
        </details>

        <details>
            <summary>Workflows</summary>
            <div id="node-workflows"></div>
        </details>


        <details>
            <summary>Required Permissions</summary>
            <ul id="node-required-permissions"></ul>
        </details>

        <!--
        <details>
            <summary>Feature Groups</summary>
            <ul id="node-feature-groups"></ul>
        </details>
            -->

        <details>
            <summary>Client Contracts</summary>
            <div id="node-client-contracts"></div>
        </details>

        <details>
            <summary>Backend Data Model</summary>
            <div id="node-backend-data-model"></div>

            <h4>Data Reads</h4>
            <ul id="node-data-reads"></ul>

            <h4>Data Writes</h4>
            <ul id="node-data-writes"></ul>
        </details>

        <details>
            <summary>Rules Engine</summary>

            <h4>Engines</h4>
            <ul id="node-rules-engines"></ul>

            <h4>Rules Purpose</h4>
            <ul id="node-rules-purpose"></ul>

            <div id="node-rules-output-dtos"></div>
        </details>

        <details open>
            <summary>Description</summary>
            <p id="node-details-description"></p>
        </details>

    </section>
</body>

</html>
"""


def _prepare_node_info(
        node_info: dict[str, Any],
) -> dict[str, dict[str, Any]]:
    prepared: dict[str, dict[str, Any]] = {}

    for node_id, node_data in node_info.items():
        if hasattr(node_data, "screen_spec"):
            prepared_node = flow_node_to_node_info(node_data)
        elif isinstance(node_data, dict):
            prepared_node = dict(node_data)
        else:
            raise TypeError(
                f"Unsupported node_info value for {node_id}: {type(node_data)}"
            )

        images = prepared_node.get("screen_images", [])

        if isinstance(images, str):
            images = [images]

        prepared_images: list[str] = []

        for image in images:
            if image.startswith(("http://", "https://", "data:")):
                prepared_images.append(image)
                continue

            image_path = IMAGES_DIR / image

            if not image_path.exists():
                print(f"[WARN] Missing image: {image_path}")
                continue

            prepared_images.append(image_to_data_uri(image_path))

        prepared_node["screen_images"] = prepared_images
        prepared[node_id] = prepared_node

    return prepared


def render_mermaid_flow_diagram(
        chart_definition: str,
        node_info: PatientFlowNodes,
        node_label_to_id: dict[str, str],
) -> None:
    css: str = _load_text(CSS_PATH)
    js: str = _load_text(JS_PATH)

    prepared_node_info = _prepare_node_info(node_info)

    config_json: str = json.dumps(
        {
            "nodeInfo": prepared_node_info,
            "nodeLabelToId": node_label_to_id,
            "chartDefinition": chart_definition,
        }
    )

    html = _get_embedded_html(config_json, js, css)

    components.html(html, height=1100, scrolling=True)
