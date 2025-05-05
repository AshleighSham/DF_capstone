const axios = require("axios");

const client_id = "47f30520c4e8485b925d9910d6d68d62";
const client_secret = "aa86334039704df3aec915153c9dd8c4";

const authOptions = {
  method: "post",
  url: "https://accounts.spotify.com/api/token",
  headers: {
    Authorization:
      "Basic " +
      Buffer.from(client_id + ":" + client_secret).toString("base64"),
    "Content-Type": "application/x-www-form-urlencoded",
  },
  data: new URLSearchParams({
    grant_type: "client_credentials",
  }),
};

axios(authOptions)
  .then((response) => {
    console.log("Access Token:", response.data.access_token);
  })
  .catch((error) => {
    console.error(
      "Error:",
      error.response ? error.response.data : error.message
    );
  });
