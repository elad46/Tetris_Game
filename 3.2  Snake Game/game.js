const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth * 0.8;
canvas.height = window.innerHeight * 0.8;
const cellSize = 20;
let snake = [{ x: 150, y: 150 }];
let direction = { x: 20, y: 0 };
let food = { x: 300, y: 300 };
let score = 0;
let gameInterval;
let speedSetting = { slow: 200, medium: 140, fast: 80 };

document.getElementById("speed").addEventListener("change", function() {
    clearInterval(gameInterval);
    gameInterval = setInterval(gameLoop, speedSetting[this.value]);
});

function startGame() {
    snake = [{ x: 150, y: 150 }];
    direction = { x: 20, y: 0 };
    placeFood();
    score = 0;
    document.getElementById("score").textContent = score;
    document.getElementById("gameOver").style.display = "none";
    clearInterval(gameInterval);
    gameInterval = setInterval(gameLoop, speedSetting[document.getElementById("speed").value]);
}

function drawSnake() {
    ctx.fillStyle = 'green';
    snake.forEach(part => ctx.fillRect(part.x, part.y, cellSize, cellSize));
}

function drawFood() {
    ctx.fillStyle = 'red';
    ctx.fillRect(food.x, food.y, cellSize, cellSize);
}

function moveSnake() {
    let head = { x: snake[0].x + direction.x * 20, y: snake[0].y + direction.y * 20 };
    snake.unshift(head);

    if (head.x === food.x && head.y === food.y) {
        placeFood();
        score++;
        document.getElementById("score").textContent = score;
    } else {
        snake.pop();
    }

    if (head.x < 0 || head.x >= canvas.width || head.y < 0 || head.y >= canvas.height || snake.slice(1).some(part => part.x === head.x && part.y === head.y)) {
        gameOver();
    }
}

function placeFood() {
    food = {
        x: Math.floor(Math.random() * (canvas.width / cellSize)) * cellSize,
        y: Math.floor(Math.random() * (canvas.height / cellSize)) * cellSize
    };
}

function gameOver() {
    clearInterval(gameInterval);
    document.getElementById("gameOver").style.display = "block";
}

function toggleTheme() {
    document.body.classList.toggle('dark-mode');
}

document.addEventListener('keydown', e => {
    switch (e.key) {
        case 'ArrowUp': if (direction.y === 0) direction = { x: 0, y: -1 }; break;
        case 'ArrowDown': if (direction.y === 0) direction = { x: 0, y: 1 }; break;
        case 'ArrowLeft': if (direction.x === 0) direction = { x: -1, y: 0 }; break;
        case 'ArrowRight': if (direction.x === 0) direction = { x: 1, y: 0 }; break;
    }
});

window.onload = startGame;
