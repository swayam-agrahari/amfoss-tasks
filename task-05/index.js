class navbar extends HTMLElement {
   connectedCallback() {
      this.innerHTML = `
     <nav class="navbar">
     <div class="logo">
         <a href="index.html"><img src="assets/logo.png" alt="Band Logo"></a>
     </div>
     <div class="social-icons">
         <a href="https://open.spotify.com/artist/53XhwfbYqKCa1cC15pYq2q"><img src="assets/navbar/spotify.svg" alt="Spotify"></a>
         <a href="https://www.youtube.com/@ImagineDragons"><img src="assets/navbar/youtube.svg" alt="YouTube"></a>
         <a href="https://twitter.com/Imaginedragons"><img src="assets/navbar/twitter.svg" alt="Twitter"></a>
         <a href="https://www.instagram.com/imaginedragons"><img src="assets/navbar/instagram.svg" alt="Instagram"></a>
     </div>
 </nav>
     `;
   }
}

customElements.define('custom-navbar', navbar);