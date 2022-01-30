import PyApp from './PyApp.svelte';

const app = new PyApp({
	target: document.body,
	props: {
		name: 'Python Webview Svelte'
	}
});

export default app;