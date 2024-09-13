export async function getData(data, output){
    return new Promise((resolve, reject) => {
        $.post({
            url: 'http://127.0.0.1:8000/upload-image/',
            data: data,
            processData: false,
            contentType: false,
        })
        .done((response) => {
            resolve(response);
        })
        .fail((error) => {
            reject(error);
        });
    });
}
