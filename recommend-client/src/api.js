const axios = require('axios');


export async function initial()   {
    try {
        const response = await axios.get('http://127.0.0.1:8000/init/');
        return response.data
      } catch (error) {
        return {'Success': false, 'Message':error}
      }
}

export async function coldStart() {
    try {
        const response = await axios.get('http://127.0.0.1:8000/coldStart/');
        return response.data
      } catch (error) {
        return {'Success': false, 'Message':error}
      }
}

export async function nextThree(book) {
    try {
        const response = await axios.post('http://127.0.0.1:8000/nextThree/',{isbn: book.isbn});
        return response.data // Handle the response data here
      } catch (error) {
        return {'Success': false, 'Message':error}
      }
}





