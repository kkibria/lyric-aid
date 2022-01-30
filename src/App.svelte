<script lang="ts">
	import { checkText } from "./py";

	export let name: string;
	let value = `Some words are *italic*, some are **bold**`;

	$: checkText(value);

	function handleClick() {
		checkText(value);
	}
</script>

<main>
	<h1>Hello {name}!</h1>
	<p>
		Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn
		how to build Svelte apps.
	</p>

	<textarea bind:value />
	<button on:click={handleClick}> Click me </button>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}

	textarea {
		width: 100%;
		height: 200px;
	}
</style>
