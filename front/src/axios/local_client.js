import axios from "axios";

const LocalClient = axios.create({
  baseURL: "http://127.0.0.1:8080",
  headers: {
    Accept: "application/json",
  },
});

export default LocalClient;
