import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
  timeout: 120000,
});

/**
 * Uploads a contract to the backend for analysis.
 *
 * @param {File} file
 * @returns {Promise<Object>}
 */
export async function scanContract(file) {
  const formData = new FormData();
  formData.append("file", file);

  const response = await api.post("/scan", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

  return response.data;
}

export default api;