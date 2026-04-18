async function ask() {
    const question = document.getElementById("question").value;
    const res = await askQuestion(question);

    document.getElementById("answer").innerHTML = `
        <p>${res.answer}</p>
    `;
}