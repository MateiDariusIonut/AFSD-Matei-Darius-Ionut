const apiUrl = "/items";

// Functie care preia valorile introduse in campurile de input
function getInputValues() {
    return {
        id: parseInt(document.getElementById("id").value), // Converteste in numar
        name: document.getElementById("nume").value.trim(), // Elimina spatiile de la inceput/sfarsit
        quantity: document.getElementById("cantitate").value.trim(),
        price: document.getElementById("pret").value.trim()
    };
}

// Goleste toate campurile de input
function clearInputs() {
    document.getElementById("id").value = "";
    document.getElementById("nume").value = "";
    document.getElementById("cantitate").value = "";
    document.getElementById("pret").value = "";
}

// Afiseaza toate produsele in tabelul HTML
function getItems() {
    fetch(apiUrl) // Trimite cerere GET catre /items
        .then(res => res.json()) // Transformare raspuns in JSON
        .then(data => {
            const tbody = document.querySelector("#itemsTable tbody");
            tbody.innerHTML = ""; // Goleste tabelul inainte sa il refaca

            // Parcurge lista de produse si construieste randurile tabelului
            data.forEach(item => {
                const row = `<tr>
                    <td>${item.id}</td>
                    <td>${item.name}</td>
                    <td>${item.quantity}</td>
                    <td>${item.price}</td>
                </tr>`;
                tbody.innerHTML += row; // Adauga randul in tabel
            });
        });
}

// Verifica daca numele este valid (doar litere si spatii)
function isValidName(name) {
    if (name.length === 0) return false;
    for (let i = 0; i < name.length; i++) {
        const c = name[i];
        if (!(c >= 'a' && c <= 'z') && !(c >= 'A' && c <= 'Z') && c !== ' ') {
            return false;
        }
    }
    return true;
}

// Verifica daca valoarea este un numar intreg pozitiv
function isPositiveInteger(value) {
    return !isNaN(value) && Number.isInteger(Number(value)) && Number(value) >= 0;
}

// Adauga un produs nou
function addItem() {
    const input = getInputValues();

    // Verifica daca toate campurile sunt completate (exceptie: id)
    if (input.name === "" || input.quantity === "" || input.price === "") {
        alert('Toate câmpurile trebuie completate! (înafară de "index")');
        return;
    }

    // Validare nume
    if (!isValidName(input.name)) {
        alert("Numele trebuie să conțină doar litere și spații.");
        return;
    }

    // Validare cantitate
    if (!isPositiveInteger(input.quantity)) {
        alert("Cantitatea trebuie să fie un număr întreg pozitiv.");
        return;
    }

    // Validare pret
    if (!isPositiveInteger(input.price)) {
        alert("Prețul trebuie să fie un număr întreg pozitiv.");
        return;
    }

    // Creeaza obiectul produsului pentru trimitere catre server
    const item = {
        name: input.name,
        quantity: parseInt(input.quantity),
        price: parseInt(input.price)
    };

    // Trimite cerere POST pentru adaugare
    fetch(apiUrl, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(item)
    })
    .then(res => {
        if (res.ok) {
            getItems(); // Reincarca lista de produse
            clearInputs(); // Goleste campurile
        } else {
            alert("Eroare la adăugare.");
        }
    });
}

// Editeaza un produs existent
function editItem() {
    const input = getInputValues();

    // Verifica daca ID-ul este completat
    if (!input.id) {
        alert("Introduceți un ID.");
        return;
    }

    // Verifica daca produsul cu acel ID exista
    fetch(`${apiUrl}/${input.id}`)
        .then(res => {
            if (!res.ok) throw new Error();
            return res.json();
        })
        .then(existingItem => {
            const updatedItem = {};

            // Daca numele a fost completat si este valid
            if (input.name !== "") {
                if (!isValidName(input.name)) {
                    alert("Nume invalid.");
                    return;
                }
                updatedItem.name = input.name;
            }

            // Daca cantitatea a fost completata si este valida
            if (input.quantity !== "") {
                if (!isPositiveInteger(input.quantity)) {
                    alert("Cantitate invalidă.");
                    return;
                }
                updatedItem.quantity = parseInt(input.quantity);
            }

            // Daca pretul a fost completat si este valid
            if (input.price !== "") {
                if (!isPositiveInteger(input.price)) {
                    alert("Preț invalid.");
                    return;
                }
                updatedItem.price = parseInt(input.price);
            }

            // Trimite cerere PUT catre server pentru actualizare
            fetch(`${apiUrl}/${input.id}`, {
                method: "PUT",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(updatedItem)
            })
            .then(res => {
                if (res.ok) {
                    getItems(); // Reincarca lista
                    clearInputs(); // Goleste campurile
                } else {
                    alert("Eroare la editare.");
                }
            });
        })
        .catch(() => alert("ID inexistent."));
}

// Sterge un produs dupa ID
function deleteItem() {
    const id = document.getElementById("id").value;
    if (!id) {
        alert("Introduceți un ID.");
        return;
    }

    // Verifica daca produsul exista
    fetch(`${apiUrl}/${id}`)
        .then(res => {
            if (!res.ok) throw new Error();
            return res.json();
        })
        .then(() => {
            // Daca exista, trimite cerere DELETE
            fetch(`${apiUrl}/${id}`, { method: "DELETE" })
                .then(res => {
                    if (res.ok) {
                        getItems(); // Reincarca lista
                        clearInputs(); // Goleste campurile
                    } else {
                        alert("Eroare la ștergere.");
                    }
                });
        })
        .catch(() => alert("ID inexistent."));
}