function like(postId){
    const likeCount = document.getElementById(`likes-count-${postId}`);
    const likeButton = document.getElementById(`like-button-${postId}`);

        fetch(`/like/${postId}`, {method: "POST" })
        .then((res) => res.json())
        .then((data) => {
            likeCount.innerHTML = data["likes"];
            if (data["liked"]) {
                likeButton.className = "fa-solid fa-heart text-danger"
            } else {
                likeButton.className = "fa-regular fa-heart text-danger"
            }
        })
        .catch((e) => alert("Please login to like the post."));

}