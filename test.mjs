import axios from "axios";

const response = await axios.get(
  "https://jsonplaceholder.typicode.com/users"
);

console.log(response.data);