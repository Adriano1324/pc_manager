import axios from "axios";

const localAgent = axios.create({
  baseURL: "http://127.0.0.1:8080/",
  headers: {
    "accept": "application/json",
    "Access-Control-Allow-Origin": "*"
  },
});

export default localAgent;
