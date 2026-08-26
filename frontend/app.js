async function loadProducts() {
    try {
        const response = await fetch("/api/products");

        const products = await response.json();

        const productsContainer = document.getElementById("products");

        productsContainer.innerHTML = "";

        products.forEach(product => {

            const productElement = document.createElement("div");

            productElement.innerHTML = `
                <h3>${product.name}</h3>
                <p>Price: ₹${product.price}</p>
            `;

            productsContainer.appendChild(productElement);
        });

    } catch (error) {
        console.error("Error loading products:", error);
    }
}

loadProducts();
