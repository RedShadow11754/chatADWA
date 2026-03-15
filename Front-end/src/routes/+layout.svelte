<script>
	import favicon from '$lib/assets/favicon.svg';
	import '../app.css';
	let { children } = $props();
</script>

<!-- npm install marked -->





<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

{@render children()}
