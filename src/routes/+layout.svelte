<script>
	import Header from './Header.svelte';
	import Footer from './Footer.svelte';
	import '../app.css';
</script>

<div class="app">
	<Header />
	<main>
		<slot />
	</main>
	<Footer />
</div>

<style>
	.app {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
		background-color: #303030;
	}

	main {
		width: 100vw;
		height: 100vh;
	}
</style>
