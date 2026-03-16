<script>
	import '../app.css';
  	import myImage from '$lib/assets/ADWA.jpg';
	let { children } = $props();
</script>

<div class="relative min-h-screen w-full overflow-hidden">
  <img 
    src={myImage} 
    alt="Background" 
    class="absolute inset-0 -z-20 h-full w-full object-cover"
  />
  
  <div class="absolute inset-0 -z-10 bg-black/50"></div>
{@render children()}
</div>


 
















<!-- <script>
	import '../app.css';
  	import myImage from '$lib/assets/ADWA.jpg';
	let { children } = $props();

</script>

<div class="relative min-h-screen w-full overflow-hidden">
  <img 
    src={myImage} 
    alt="Background" 
    class="absolute inset-0 -z-10 h-full w-full object-cover"
  />
  
  <div class="absolute inset-0 -z-10 bg-black/50"></div>
</div>



{@render children()} -->





