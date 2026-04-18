async function loadBooks() {
    const books = await getBooks();
    const container = document.getElementById("books");

    container.innerHTML = books.map(book => `
        <div class="bg-white p-4 rounded shadow">
            <h2 class="text-xl font-bold">${book.title}</h2>
            <p class="text-gray-600">${book.author}</p>
            <p class="mt-2 text-sm">${book.description || "No description"}</p>

            <a href="book.html?id=${book.id}" 
               class="text-blue-500 mt-3 inline-block">View Details →</a>
        </div>
    `).join("");
}

loadBooks();