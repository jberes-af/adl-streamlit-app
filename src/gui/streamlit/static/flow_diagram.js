// /src/gui/streamlit/static/flow_diagram.js

import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs";

mermaid.initialize({
    startOnLoad: false,
    securityLevel: "loose"
});

function showNodeDetails(nodeId) {
    const info = window.patientFlowConfig.nodeInfo[nodeId];
    if (!info) return;

    setText("node-details-title", info.title || nodeId);


    const screenSpec = info.screen_spec || {};

    setText(
        "node-screen-spec",
        screenSpec.purpose || "No screen specification available."
    );

    renderStringList(
        "node-screen-displayed-data",
        screenSpec.displayed_data || []
    );

    renderStringList(
        "node-screen-user-inputs",
        screenSpec.user_inputs || []
    );

    setText(
        "node-screen-primary-action",
        screenSpec.primary_action || "None specified."
    );

    renderStringList(
        "node-screen-secondary-actions",
        screenSpec.secondary_actions || []
    );

    renderStringList(
        "node-screen-validation-rules",
        screenSpec.validation_rules || []
    );

    renderStringList(
        "node-screen-navigation-in",
        screenSpec.navigation_in || []
    );

    renderNavigationRoutes(
        "node-screen-navigation-out",
        screenSpec.navigation_out || []
    );

    setText(
        "node-screen-empty-state",
        screenSpec.states?.empty_state || "None specified."
    );

    setText(
        "node-screen-loading-state",
        screenSpec.states?.loading_state || "None specified."
    );

    setText(
        "node-screen-error-state",
        screenSpec.states?.error_state || "None specified."
    );


    // renderPrimaryActions("node-primary-actions", info.primary_actions || []);
    // renderUsers("node-users", info.user_roles || info.users || []);
    renderUseCases("node-use-cases", info.use_cases || []);
    renderWorkflows("node-workflows", info.workflows || []);
    renderStringList("node-feature-groups", info.feature_groups || []);

    renderDataObjects("node-client-contracts", [
        ["Request DTOs", info.client_contracts?.request_dtos || []],
        ["Response DTOs", info.client_contracts?.response_dtos || []],
        ["Screen DTOs", info.client_contracts?.screen_dtos || []]
    ]);

    renderDataObjects("node-backend-data-model", [
        ["Definition DTOs", info.backend_data_model?.definition_dtos || []],
        ["Persistence DTOs", info.backend_data_model?.persistence_dtos || []]
    ]);


    renderDataReads(
        "node-data-reads",
        info.backend_data_model?.data_reads || []
    );

    renderDataWrites(
        "node-data-writes",
        info.backend_data_model?.data_writes || []
    );

    renderPermissions(
        "node-required-permissions",
        info.required_permissions || []
    );

    renderStringList(
        "node-data-reads",
        info.backend_data_model?.data_reads || []
    );

    renderStringList(
        "node-data-writes",
        info.backend_data_model?.data_writes || []
    );

    renderStringList(
        "node-rules-engines",
        info.rules_engine?.engines || []
    );

    renderStringList(
        "node-rules-purpose",
        info.rules_engine?.rules_purpose || []
    );

    renderDataObjects("node-rules-output-dtos", [
        ["Rules Output DTOs", info.rules_engine?.output_dtos || []]
    ]);

    renderImages(
        info.screen_images || info.images || [],
        info.title || nodeId
    );

    setText(
        "node-details-description",
        info.description || "No description available."
    );

    document.getElementById("node-details-frame").classList.remove("hidden");
}

function setText(elementId, value) {
    const element = document.getElementById(elementId);
    if (element) {
        element.textContent = value;
    }
}

function renderStringList(elementId, items) {
    const container = document.getElementById(elementId);
    if (!container) return;

    container.innerHTML = "";

    if (!items || items.length === 0) {
        container.appendChild(createMutedListItem("None specified."));
        return;
    }

    items.forEach((value) => {
        const item = document.createElement("li");
        item.textContent = value;
        container.appendChild(item);
    });
}

function renderPrimaryActions(elementId, actions) {
    const container = document.getElementById(elementId);
    if (!container) return;

    container.innerHTML = "";

    if (!actions || actions.length === 0) {
        container.appendChild(createMutedText("No actions defined."));
        return;
    }

    actions.forEach((action) => {
        const item = document.createElement("li");
        item.textContent = action;
        container.appendChild(item);
    });
}

function renderUsers(elementId, users) {
    const container = document.getElementById(elementId);
    if (!container) return;

    container.innerHTML = "";

    if (!users || users.length === 0) {
        container.appendChild(createMutedListItem("No users specified."));
        return;
    }

    users.forEach((user) => {
        const item = document.createElement("li");

        if (typeof user === "string") {
            item.textContent = user;
        } else {
            const name = user.name || "Unnamed user";
            const responsibilities = user.responsibilities || user.roles || "";

            item.textContent = responsibilities
                ? `${name} (${responsibilities})`
                : name;
        }

        container.appendChild(item);
    });
}

function renderNavigationRoutes(elementId, routes) {
    const container = document.getElementById(elementId);
    if (!container) return;

    container.innerHTML = "";

    if (!routes || routes.length === 0) {
        container.appendChild(createMutedListItem("No navigation routes specified."));
        return;
    }

    routes.forEach((route) => {
        const item = document.createElement("li");

        const parts = [
            route.action || "Unnamed action",
            route.target_screen_id ? `→ ${route.target_screen_id}` : "",
            route.condition ? `if ${route.condition}` : "",
            route.notes ? `(${route.notes})` : "",
        ].filter(Boolean);

        item.textContent = parts.join(" ");
        container.appendChild(item);
    });
}

function renderPermissions(elementId, permissions) {
    const container = document.getElementById(elementId);
    if (!container) return;

    container.innerHTML = "";

    if (!permissions || permissions.length === 0) {
        container.appendChild(createMutedListItem("No permissions specified."));
        return;
    }

    permissions.forEach((permission) => {
        const item = document.createElement("li");
        item.textContent = `${permission.domain}:${permission.action}`;
        container.appendChild(item);
    });
}

function renderDataReads(elementId, reads) {
    const container = document.getElementById(elementId);
    if (!container) return;

    container.innerHTML = "";

    if (!reads || reads.length === 0) {
        container.appendChild(createMutedText("No data reads defined."));
        return;
    }

    reads.forEach((read) => {
        const card = document.createElement("div");
        card.className = "detail-card";

        const title = document.createElement("h4");
        title.textContent = read.name || "Unnamed read";
        card.appendChild(title);

        if (read.description) {
            const description = document.createElement("p");
            description.textContent = read.description;
            card.appendChild(description);
        }

        if (read.output_dto) {
            const output = document.createElement("p");
            output.className = "muted";
            output.textContent = `Output DTO: ${read.output_dto}`;
            card.appendChild(output);
        }

        if (read.source_dtos && read.source_dtos.length > 0) {
            const sources = document.createElement("p");
            sources.className = "muted";
            sources.textContent = `Sources: ${read.source_dtos.join(", ")}`;
            card.appendChild(sources);
        }

        container.appendChild(card);
    });
}

function renderDataWrites(elementId, writes) {
    const container = document.getElementById(elementId);
    if (!container) return;

    container.innerHTML = "";

    if (!writes || writes.length === 0) {
        container.appendChild(createMutedText("No data writes defined."));
        return;
    }

    writes.forEach((write) => {
        const card = document.createElement("div");
        card.className = "detail-card";

        const title = document.createElement("h4");
        title.textContent = write.name || "Unnamed write";
        card.appendChild(title);

        if (write.description) {
            const description = document.createElement("p");
            description.textContent = write.description;
            card.appendChild(description);
        }

        if (write.target_dtos && write.target_dtos.length > 0) {
            const targets = document.createElement("p");
            targets.className = "muted";
            targets.textContent = `Targets: ${write.target_dtos.join(", ")}`;
            card.appendChild(targets);
        }

        container.appendChild(card);
    });
}

function renderUseCases(elementId, useCases) {
    const container = document.getElementById(elementId);
    if (!container) return;

    container.innerHTML = "";

    if (!useCases || useCases.length === 0) {
        container.appendChild(createMutedText("No use cases specified."));
        return;
    }

    useCases.forEach((useCase) => {
        const card = document.createElement("div");
        card.className = "detail-card";

        const title = document.createElement("h4");
        title.textContent = useCase.name || "Unnamed use case";

        const description = document.createElement("p");
        description.textContent = useCase.description || "";

        card.appendChild(title);

        if (useCase.description) {
            card.appendChild(description);
        }

        if (useCase.outcome) {
            const outcome = document.createElement("p");
            outcome.textContent = `Outcome: ${useCase.outcome}`;
            outcome.className = "muted";
            card.appendChild(outcome);
        }

        container.appendChild(card);
    });
}

function renderWorkflows(elementId, workflows) {
    const container = document.getElementById(elementId);
    if (!container) return;

    container.innerHTML = "";

    if (!workflows || workflows.length === 0) {
        container.appendChild(createMutedText("No workflows specified."));
        return;
    }

    workflows.forEach((workflow) => {
        const card = document.createElement("div");
        card.className = "detail-card";

        const title = document.createElement("h4");
        title.textContent = workflow.id
            ? `${workflow.id}: ${workflow.name}`
            : workflow.name || "Unnamed workflow";
        card.appendChild(title);

        if (workflow.description) {
            const description = document.createElement("p");
            description.textContent = workflow.description;
            card.appendChild(description);
        }

        const metaParts = [];

        if (workflow.goal) metaParts.push(`Goal: ${workflow.goal}`);
        if (workflow.trigger) metaParts.push(`Trigger: ${workflow.trigger}`);
        if (workflow.success_outcome) metaParts.push(`Outcome: ${workflow.success_outcome}`);

        if (metaParts.length > 0) {
            const meta = document.createElement("p");
            meta.className = "muted";
            meta.textContent = metaParts.join(" | ");
            card.appendChild(meta);
        }

        if (workflow.flow && workflow.flow.length > 0) {
            const details = document.createElement("details");
            const summary = document.createElement("summary");
            summary.textContent = "Flow Steps";
            details.appendChild(summary);

            const list = document.createElement("ol");

            workflow.flow.forEach((step) => {
                const item = document.createElement("li");
                item.textContent = `${step.actor}: ${step.action}`;
                if (step.system_response) {
                    item.textContent += ` → ${step.system_response}`;
                }
                list.appendChild(item);
            });

            details.appendChild(list);
            card.appendChild(details);
        }

        container.appendChild(card);
    });
}

function renderDataObjects(elementId, groupedDataObjects) {
    const container = document.getElementById(elementId);
    if (!container) return;

    container.innerHTML = "";

    let hasAny = false;

    groupedDataObjects.forEach(([groupTitle, dataObjects]) => {
        if (!dataObjects || dataObjects.length === 0) return;

        hasAny = true;

        const group = document.createElement("div");
        group.className = "dto-group";

        const heading = document.createElement("h4");
        heading.textContent = groupTitle;
        group.appendChild(heading);

        dataObjects.forEach((dataObject) => {
            const card = document.createElement("div");
            card.className = "data-object-card";

            const title = document.createElement("h4");
            title.textContent = dataObject.name || "Unnamed data object";
            card.appendChild(title);

            if (dataObject.description) {
                const description = document.createElement("p");
                description.textContent = dataObject.description;
                description.className = "data-object-description";
                card.appendChild(description);
            }

            if (dataObject.code) {
                const dtoDetails = document.createElement("details");
                dtoDetails.open = true;

                const dtoSummary = document.createElement("summary");
                dtoSummary.textContent = "DTO";
                dtoDetails.appendChild(dtoSummary);

                const pre = document.createElement("pre");
                const code = document.createElement("code");
                code.textContent = dataObject.code;
                pre.appendChild(code);

                dtoDetails.appendChild(pre);
                card.appendChild(dtoDetails);
            }

            if (dataObject.json_example) {
                const jsonDetails = document.createElement("details");

                const jsonSummary = document.createElement("summary");
                jsonSummary.textContent = "JSON Example";
                jsonDetails.appendChild(jsonSummary);

                const pre = document.createElement("pre");
                const code = document.createElement("code");
                code.textContent = dataObject.json_example;
                pre.appendChild(code);

                jsonDetails.appendChild(pre);
                card.appendChild(jsonDetails);
            }

            if (!dataObject.description && !dataObject.code && !dataObject.json_example) {
                card.appendChild(createMutedText("No details provided."));
            }

            group.appendChild(card);
        });

        container.appendChild(group);
    });

    if (!hasAny) {
        container.appendChild(createMutedText("No data models specified."));
    }
}

function renderImages(images, title) {
    const imageContainer = document.getElementById("node-details-images");
    const imageEmpty = document.getElementById("node-details-image-empty");

    if (!imageContainer || !imageEmpty) return;

    imageContainer.innerHTML = "";

    if (!images || images.length === 0) {
        imageEmpty.classList.remove("hidden");
        return;
    }

    imageEmpty.classList.add("hidden");

    images.forEach((imageSrc, index) => {
        const image = document.createElement("img");
        image.src = imageSrc;
        image.alt = `${title || "Screen sketch"} ${index + 1}`;
        image.className = "details-image";

        imageContainer.appendChild(image);
    });
}

function createMutedText(text) {
    const paragraph = document.createElement("p");
    paragraph.textContent = text;
    paragraph.className = "muted";
    return paragraph;
}

function createMutedListItem(text) {
    const item = document.createElement("li");
    item.textContent = text;
    item.className = "muted";
    return item;
}

function findNodeIdFromMermaidNode(node) {
    if (!node) return null;

    const {nodeInfo, nodeLabelToId} = window.patientFlowConfig;

    const matchedByGeneratedId = Object.keys(nodeInfo).find((nodeId) =>
        node.id && node.id.includes(nodeId)
    );

    if (matchedByGeneratedId) return matchedByGeneratedId;

    const labelText = node.textContent.trim().replace(/\s+/g, " ");
    return nodeLabelToId[labelText] || null;
}

function bindChartClickHandler() {
    const chart = document.getElementById("chart");
    if (!chart) return;

    chart.addEventListener("click", (event) => {
        const node = event.target.closest(".node");
        const nodeId = findNodeIdFromMermaidNode(node);

        if (nodeId) {
            showNodeDetails(nodeId);
        }
    });
}

async function init() {
    if (!window.patientFlowConfig) {
        console.error("Missing patientFlowConfig.");
        return;
    }

    const chart = document.getElementById("chart");
    if (!chart) {
        console.error("Missing chart container.");
        return;
    }

    const {chartDefinition} = window.patientFlowConfig;

    try {
        const {svg} = await mermaid.render("patient-flow-chart", chartDefinition);
        chart.innerHTML = svg;
        bindChartClickHandler();
    } catch (error) {
        console.error("Mermaid render failed:", error);
        chart.innerHTML = "<p class='muted'>Unable to render flow diagram.</p>";
    }
}

if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
} else {
    init();
}

