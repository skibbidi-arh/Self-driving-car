class Car {
    constructor(x, y, width, height) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.controls=new Controls()
    }

    update() {  // ✅ Ensure this is inside the Car class
        if (this.controls.forward) {
            this.y -= 2;
        }
        if (this.controls.reverse) {
            this.y += 2;
        }
        if (this.controls.left) {
            this.x -= 2;
        }
        if (this.controls.right) {
            this.x += 2;
        }

    }
    

    draw(ctx) {
        ctx.fillStyle = "blue"; // Set color to make it visible
        ctx.beginPath();
        ctx.rect(
            this.x - this.width / 2,
            this.y - this.height / 2,
            this.width,
            this.height
        );
        ctx.fill();
    }
}
