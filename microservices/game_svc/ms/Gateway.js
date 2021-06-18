const url = process.env.API_GATEWAY || 'http://host.docker.internal:8090';
const users = url + '/users/api/v1'
const axios = require('axios')

module.exports = {
    url: url,
    users: users,

    getUser(name) {
        return axios.get(`${users}/user/${name}`)
    },
    createUser(name, address) {
        return axios.post(`${users}/user`, {username: name, origin_ip: address, last_ip: address})
    },
    updateUser(name, address) {
        return axios.put(`${users}/user/${name}`, {ip: address})
    }
}
