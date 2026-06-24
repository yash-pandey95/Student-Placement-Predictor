document
.getElementById("predictBtn")
.addEventListener("click", async () => {

    const card =
    document.getElementById("resultCard");

    card.innerHTML = "⏳ Predicting...";
    card.style.background = "#fff3cd";
    card.style.color = "#856404";

    const data = {

        gender: parseInt(
            document.getElementById("gender").value
        ),

        age: parseInt(
            document.getElementById("age").value
        ),

        tenth_percentage: parseFloat(
            document.getElementById("tenth_percentage").value
        ),

        twelfth_percentage: parseFloat(
            document.getElementById("twelfth_percentage").value
        ),

        degree_percentage: parseFloat(
            document.getElementById("degree_percentage").value
        ),

        internships_count: parseInt(
            document.getElementById("internships_count").value
        ),

        projects_count: parseInt(
            document.getElementById("projects_count").value
        ),

        city_tier:
        document.getElementById("city_tier").value,

        degree_field:
        document.getElementById("degree_field").value
    };

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/predict",
            {
                method:"POST",
                headers:{
                    "Content-Type":"application/json"
                },
                body:JSON.stringify(data)
            }
        );

        const result = await response.json();

        if(result.prediction === "Placed")
        {
            card.innerHTML =
            "🎉 PLACED 🎉";

            card.style.background =
            "#d4edda";

            card.style.color =
            "#155724";

            card.animate(
            [
                {transform:"scale(1)"},
                {transform:"scale(1.1)"},
                {transform:"scale(1)"}
            ],
            {
                duration:1000
            });

        }
        else
        {
            card.innerHTML =
            "❌ NOT PLACED";

            card.style.background =
            "#f8d7da";

            card.style.color =
            "#721c24";
        }

    }
    catch(error)
    {
        card.innerHTML =
        "⚠️ Backend Connection Error";

        card.style.background =
        "#f8d7da";

        card.style.color =
        "#721c24";

        console.log(error);
    }

});