<<<<<<< HEAD
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
=======
$(function(){
    const uploadInput = $("#input_file");
    const submitButton = $("#submit");
    const output = $(".output");
    
    output.text("sem status");
    
    submitButton.on("click", async function(event){
        event.preventDefault();
    
        let formData = new FormData();
        formData.append('file', uploadInput[0].files[0]);
    

        let data = await get_data(formData, output)
        console.log(data)
    //     $.post({
    //         url: 'http://127.0.0.1:8000/upload-image/',
    //         type: 'POST',
    //         data: formData,
    //         processData: false,
    //         contentType: false,
    //     })
    //     .done(async function(response) {
    //         console.log(response);
    //         output.text("Upload bem-sucedido!");
    //     })
    //     .fail(async function(error) {
    //         console.log(error);
    //         output.text("Erro no upload.");
    //     })
    // });

    })
})


async function get_data(data, output){
    return new Promise((resolve,reject)=>{
        $.post({
            url: 'http://127.0.0.1:8000/upload-image/',
            data: data,
            processData: false,
            contentType: false,
        })
        .done((response)=>{
            resolve({
                "data":response
            });
            output.text(`${response.prediction['confidence']}%`);
        })
        .fail((error)=>{
            reject({"data":error})
        });
        output.text("Erro no upload.");
    })
}


>>>>>>> e4d4ecdc6d7c33d82078296d87346851e992c351
