$(document).ready(function(){
    const uploadInput = $("#input_file");
    const submitButton = $("#submit");
    const output = $(".output");

    output.text("sem status")

    submitButton.on("click", async function(event){
        event.preventDefault();
        let formData = new FormData();
        formData.append('file', uploadInput[0].files[0]);
        console.log(formData)

        fetch('http://127.0.0.1:8000/upload-image/', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Error:', error));
    });
});
