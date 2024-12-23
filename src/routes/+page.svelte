<script>
	import { spring } from 'svelte/motion';
	import { onMount } from 'svelte';

	let count = -1;

	const displayed_count = spring();
	$: displayed_count.set(count);
	$: offset = modulo($displayed_count, 1);

	function modulo(n, m) {
		// handle negative numbers
		return ((n % m) + m) % m;
	}

	async function fetchCount() {
		try {
			const res = await fetch('https://analytics.jonasjones.dev/requests/get/count');
			if (res.ok) {
				const data = await res.json();
				count = data.count;
			}
		} catch (error) {
			console.error('Error fetching count:', error);
		}
	}

	onMount(() => {
		// Fetch initial count
		fetchCount();

		// Update the count every 3 seconds
		const interval = setInterval(fetchCount, 10000);

		// Cleanup when component is destroyed
		return () => clearInterval(interval);
	});
</script>

<h1 class="counterheader">jonasjones.dev Ecosystem Requests</h1>

<div class="counter">

	<div class="counter-viewport">
		<div class="counter-digits" style="transform: translate(0, {100 * offset}%)">
			<strong class="hidden" aria-hidden="true">{Math.floor($displayed_count + 1)}</strong>
			<strong>{Math.floor($displayed_count)}</strong>
		</div>
	</div>
</div>

<style>
  .counterheader {
    color: white;
    text-align: center;
    font-size: 2rem;
    margin-top: 40vh;
  }
	.counter {
		display: flex;
		border: 5px solid green;
    border-radius: 10px;
		margin: 5rem;
    margin-top: 0;
    justify-content: center;
    align-items: center;
    background-color: #000;
	}

	svg {
		width: 25%;
		height: 25%;
	}

	path {
		vector-effect: non-scaling-stroke;
		stroke-width: 2px;
		stroke: #444;
	}

	.counter-viewport {
		width: 32em;
		height: 8em;
		overflow: hidden;
		text-align: center;
		position: relative;
	}

	.counter-viewport strong {
		position: absolute;
		display: flex;
		width: 100%;
		height: 100%;
		font-weight: 400;
		color: white;
		font-size: 8rem;
		align-items: center;
		justify-content: center;
	}

	.counter-digits {
		position: absolute;
		width: 100%;
		height: 100%;
	}

	.hidden {
		top: -100%;
		user-select: none;
	}
</style>
