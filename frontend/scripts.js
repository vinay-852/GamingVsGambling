async function classifyGame() {
    const gameName = document.getElementById("gameName").value;
    const resultElement = document.getElementById("result");
    const loadingElement = document.getElementById("loading");
    const animationElement = document.querySelector(".animation");
    
    resultElement.innerText = '';
    loadingElement.classList.remove('hidden');
    animationElement.classList.add('active');
    
    try {
        const response = await fetch(`https://gamingvsgambling.onrender.com/classify?game_name=${encodeURIComponent(gameName)}`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        resultElement.innerHTML = `
            <strong>Classification:</strong> ${data.result.classification}<br>
            <strong>Explanation from App Description:</strong> ${data.result.explaination_from_app_description}<br>
            <strong>Explanation from App Permissions:</strong> ${data.result.explaination_from_app_permissions}<br>
            <strong>Explanation from App Reviews:</strong> ${data.result.explaination_from_app_reviews}
        `;
    } catch (error) {
        resultElement.innerText = `Error: ${error.message}`;
    } finally {
        loadingElement.classList.add('hidden');
        animationElement.classList.remove('active');
    }
}

document.getElementById("gameName").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        classifyGame();
    }
});
