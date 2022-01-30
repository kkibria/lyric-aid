<script lang="ts">
	import App from "./App.svelte";
	import { ready } from "./py";
	export let name: string;
</script>

{#if $ready}
	<App {name} />
{/if}
