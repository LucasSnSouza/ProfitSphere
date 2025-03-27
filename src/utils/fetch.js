export default{
    
    async request(url, method = 'GET', body = null, headers = {}) {
        const options = {
          method: method,
          headers: {
            'Content-Type': 'application/json',
            ...headers,
          },
          body: body ? JSON.stringify(body) : null,
        }
        return fetch(`http://localhost:5000${url}`, options)
          .then(response => {
            if (!response.ok) {
              return Promise.reject(`Erro na requisição: ${response.statusText}`)
            }
            return response.json()
          })
          .catch(error => {
            console.error('Erro ao realizar requisição:', error)
            throw error
          })
      }    

}