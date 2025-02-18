function attachEvents() {
    const buttonLoadPosts = document.querySelector("#btnLoadPosts");
    const buttonViewPosts = document.querySelector("#btnViewPost");
    const selectPosts = document.querySelector("#posts");

    const baseURL = `http://localhost:3030/jsonstore/blog`;
    const postsEndpoint = `/posts`;
    const commentsEndpoint = `/comments`;

    const postTitle = document.querySelector("#post-title");
    const postBody = document.querySelector("#post-body");
    const postComments = document.querySelector("#post-comments");

    buttonLoadPosts.addEventListener("click", () => {
        selectPosts.innerHTML = "";

        fetch(baseURL + postsEndpoint)
            .then(response => response.json())
            .then(postsData => {
                Object.keys(postsData).forEach(id => {
                    const optionElement = document.createElement("option");
                    optionElement.value = id;
                    optionElement.textContent = postsData[id].title;
                    selectPosts.append(optionElement);
                });
            })
            .catch(error => console.error("Error loading posts:", error));
    });

    buttonViewPosts.addEventListener("click", () => {
        const selectedPostId = selectPosts.value; 

        fetch(baseURL + postsEndpoint)
            .then(response => response.json())
            .then(postsData => {
                const selectedPost = postsData[selectedPostId];

                postTitle.textContent = selectedPost.title;
                postBody.textContent = selectedPost.body;

                return fetch(baseURL + commentsEndpoint);
            })
            .then(response => response.json())
            .then(commentsData => {
                const filteredComments = Object.values(commentsData).filter(
                    comment => comment.postId === selectedPostId
                );

                postComments.innerHTML = "";

                filteredComments.forEach(comment => {
                    const li = document.createElement("li");
                    li.textContent = comment.text;
                    postComments.appendChild(li);
                });
            })
            .catch(error => console.error("Error viewing post:", error));
    });
}

attachEvents();
