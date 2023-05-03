import axios from "axios"
const LOCAL_URL = "http://localhost:8000/"
let BACKEND_URL = (process.env.BACKEND_URL || LOCAL_URL) + "api/"
const headers = { "Content-Type": "application/json" }

function handleErrors(error: any) {
  if (error.response) {
    // Response status is an error code
    console.log(error.response.status)
  } else if (error.request) {
    // Response not received though the request was sent
    console.log(error.request)
  } else {
    // An error occurred when setting up the request
    console.log(error.message)
  }
}

export async function getAllUsers() {
  try {
    const response = await axios.get(BACKEND_URL + "getAllUsers/", {
      headers: headers,
    })
    return response.data
  } catch (error) {
    handleErrors(error)
  }
}

export async function getMessagesForUser(userId: string) {
  try {
    const response = await axios.get(BACKEND_URL + "getMessagesForUser/", {
      headers: headers,
      params: { userId: userId },
    })
    return response.data
  } catch (error) {
    handleErrors(error)
    return []
  }
}

export async function selectAction(userId: string, actionId: number) {
  try {
    const response = await axios.post(
      BACKEND_URL + "selectAction/",
      {
        actionId: actionId,
        userId: userId,
      },
      { headers: headers }
    )
    return response.data
  } catch (error) {
    handleErrors(error)
  }
}

export async function recordClickEvent(userId: string, actionId: number) {
  try {
    const response = await axios.post(
      BACKEND_URL + "recordClickEvent/",
      {
        actionId: actionId,
        userId: userId,
      },
      { headers: headers }
    )
    return response.data
  } catch (error) {
    handleErrors(error)
  }
}

export async function recordImpression(userId: string, promptId: number) {
  try {
    const response = await axios.post(
      BACKEND_URL + "recordImpression/",
      {
        promptId: promptId,
        userId: userId,
      },
      { headers: headers }
    )
    return response.data
  } catch (error) {
    handleErrors(error)
  }
}
