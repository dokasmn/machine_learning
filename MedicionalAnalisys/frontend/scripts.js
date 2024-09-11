$(document).ready(async function(){
    const uploadInput = $("#input_file");
    const submitButton = $("#submit");

    submitButton.on("click", async function(event){
        event.preventDefault();
        console.log("ksjdhfkjhskjdhfjksdfhksjdhfjkhskdjfhjkdsd")
        let formData = new FormData();
        formData.append('image_file', uploadInput[0].files);
        $.post({
            url: '/upload-image/',
            data: formData
        })
        .done(function(response){
            console.log(response);
        })
        .fail(function(error){
            console.log(error);
        })
    })
})