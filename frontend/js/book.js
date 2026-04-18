const params = new URLSearchParams(window.location.search);
const id = params.get("id");

async function loadBook() {
    const book = await getBook(id);
    const container = document.getElementById("book");

    container.innerHTML = `
        <h1 class="text-2xl font-bold">${book.title}</h1>
        <p class="text-gray-600">${book.author}</p>

        <p class="mt-4">${book.description}</p>

        <a href="${book.book_url}" target="_blank" 
           class="text-blue-500 mt-4 inline-block">Read Book</a>
    `;
}

loadBook();