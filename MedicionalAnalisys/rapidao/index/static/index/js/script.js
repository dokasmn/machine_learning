$(function() {
    const uploadInput = $("#input_file");
    const submitButton = $("#submit");
    const output = $(".output");

    output.text("sem status");

    submitButton.on("click", async function(event) {
        event.preventDefault();

        let formData = new FormData();
        formData.append('file', uploadInput[0].files[0]);

        try {
            let response = await get_data(formData);
            console.log(response);
            output.text("Upload bem-sucedido!");
        } catch (error) {
            console.log(error);
            output.text("Erro no upload.");
        }
    });
});

async function get_data(formData) {
    try {
        const response = await fetch('/upload-image/', {
            method: 'POST',
            body: formData,
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        return data;
    } catch (error) {
        throw error;
    }
}
