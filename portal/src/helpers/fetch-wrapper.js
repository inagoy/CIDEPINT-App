import { useAuthStore } from '@/stores/auth';


export const fetchWrapper = {
    get: request('GET'),
    post: request('POST'),
    put: request('PUT'),
    delete: request('DELETE')
};

/**
 * Creates a request function that can be used to make HTTP requests.
 *
 * @param {string} method - The HTTP method to use for the request.
 * @return {function} - The request function that takes in a URL and an optional request body.
 */
function request(method) {
    return (url, body) => {
        const requestOptions = {
            method,
            headers: authHeader(url)
        };
        if (body) {
            requestOptions.headers['Content-Type'] = 'application/json';
            requestOptions.body = JSON.stringify(body);
        }
        return fetch(url, requestOptions).then(handleResponse);
    }
}

/**
 * Returns the authorization header with the JWT token if the user is logged in and the request is to the API URL.
 *
 * @param {string} url - The URL of the request
 * @return {object} The authorization header object containing the JWT token
 */
function authHeader(url) {
    const { user } = useAuthStore();
    const isLoggedIn = !!user?.token;
    const isApiUrl = url.startsWith(import.meta.env.VITE_API_URL);
    if (isLoggedIn && isApiUrl) {
        return { Authorization: `Bearer ${user.token}` };
    } else {
        return {};
    }
}

/**
 * Handles the response from an API call.
 *
 * @param {Response} response - The response object from the API call.
 * @return {Promise} A promise that resolves to the parsed data from the response, or rejects with an error.
 */
function handleResponse(response) {
    return response.text().then(text => {
        const data = text && JSON.parse(text);
        
        if (!response.ok) {
            const error = data.error
            return Promise.reject(error);
        }
        return data;
    });
}    
