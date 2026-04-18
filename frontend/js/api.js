const BASE_URL = "http://127.0.0.1:8000/api";

// Get all books
async function getBooks() {
    const res = await fetch(`${BASE_URL}/books/`);
    return await res.json();
}

// Get single book
async function getBook(id) {
    const res = await fetch(`${BASE_URL}/books/${id}/`);
    return await res.json();
}

// Ask question
async function askQuestion(question) {
    const res = await fetch(`${BASE_URL}/ask/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ question })
    });
    return await res.json();
}