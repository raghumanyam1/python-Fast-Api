import axios from "axios";

const api = axios.create({
  baseURL: "https://jsonplaceholder.typicode.com",
});

api.interceptors.request.use(
  (config) => {

    const token = "abc123";

    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }

    console.log("Request interceptor executed!");

    return config;
  },
  (error) => Promise.reject(error)
);

const response = await api.get("/users");

console.log(response.data);