import { getData } from './requests.js';  // Certifique-se de que o caminho está correto

$(function(){
    const uploadInput = $("#input_file");
    const submitButton = $("#submit");
    const output = $(".output");
    
    output.text("sem status");
    
    submitButton.on("click", async function(event){
        event.preventDefault();
    
        let formData = new FormData();
        formData.append('file', uploadInput[0].files[0]);
    
        try {
            let analisys = await getData(formData, output);
            if (analisys.prediction) {
                const confidence = analisys.confidence['confidence'].toFixed(2);
                output.text(`${confidence}%`);
            } else {
                output.text('Ocorreu um erro');
            }
        } catch (error) {
            output.text('Erro ao processar os dados');
            console.error(error);
        }
    });
});
