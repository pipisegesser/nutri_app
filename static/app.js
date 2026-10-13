document.addEventListener("DOMContentLoaded", () => {
    cargarPacientes();

    const form = document.getElementById("pacienteForm");
    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const nuevoPaciente = {
            nombre: document.getElementById("nombre").value,
            apellido: document.getElementById("apellido").value,
            edad: parseInt(document.getElementById("edad").value),
            email: document.getElementById("email").value,
            telefono: document.getElementById("telefono").value,
            objetivo: document.getElementById("objetivo").value
        };

        try {
            const response = await fetch("/pacientes/", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(nuevoPaciente)
            });

            if (response.ok) {
                form.reset();
                cargarPacientes();
            } else {
                const err = await response.json();
                alert("Error: " + err.detail);
            }
        } catch (error) {
            console.error("Error al guardar:", error);
        }
    });
});

async function cargarPacientes() {
    try {
        const response = await fetch("/pacientes/");
        const pacientes = await response.json();

        const tbody = document.getElementById("tablaPacientes");
        tbody.innerHTML = "";

        pacientes.forEach(p => {
            const tr = document.createElement("tr");
            tr.innerHTML = `
                <td><strong>${p.apellido}, ${p.nombre}</strong></td>
                <td>${p.edad} años</td>
                <td>${p.email}<br><small>${p.telefono || '-'}</small></td>
                <td>${p.objetivo || '-'}</td>
            `;
            tbody.appendChild(tr);
        });
    } catch (error) {
            console.error("Error al cargar pacientes:", error);
    }
}