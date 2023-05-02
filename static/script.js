"use strict";

const $cupcakeList = $("#cupcakes");
const $newCupcakeForm = $("#new-cupcake");
const BASE_URL = "http://localhost:5000/"

$newCupcakeForm.on("submit", async function handleFormSubmit(evt) {
  evt.preventDefault();
  await addNewCupcake();
});

async function addNewCupcake() {
  const flavor = $("#flavor").val();
  const size = $("#size").val();
  const rating = $("#rating").val();
  const imageUrl = $("#image-url").val();

  await axios.post(BASE_URL, {data:{
    flavor,
    size,
    rating,
    imageUrl
  }})
}

async function displayCupcakes() {
  const cupcakes = await axios.get(`${BASE_URL}api/cupcakes`);

  
}