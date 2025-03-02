const canvas = document.getElementById("myCanvas");
canvas.height = window.innerHeight;
canvas.width = 400; // Increased width

const ctx = canvas.getContext("2d");

const car = new Car(200, 200, 50, 80); // Adjust position
car.draw(ctx);

animate ();

function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear the previous frame
    car.update();
    car.draw(ctx);
    requestAnimationFrame(animate);
}



