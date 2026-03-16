<script>
  // Reactive variables
  let name = '';
  let email = '';
  let feed = '';
  let statusMessage = '';
  let isSending = false;

  // Refs for manual DOM clearing (fallback)
  let nameInput, emailInput, feedInput;

  async function sendFeedback(event) {
    // Explicitly prevent default form submission
    event.preventDefault();

    // Validation
    if (!feed || !name) {
      statusMessage = "❌ Name and message are required!";
      return;
    }

    isSending = true;
    statusMessage = "⏳ Sending...";

    const params = new URLSearchParams({
      feed,
      name,
      email: email || "No Email"
    });

    try {
      const res = await fetch(`http://127.0.0.1:8000/feedback/?${params.toString()}`);

      if (res.ok) {
        const data = await res.json();

        // Success – clear all fields and show message
        statusMessage = "✅ Feedback sent successfully!";

        // Clear reactive variables (should update bindings)
        name = '';
        email = '';
        feed = '';

        // Fallback: manually clear input DOM elements
        if (nameInput) nameInput.value = '';
        if (emailInput) emailInput.value = '';
        if (feedInput) feedInput.value = '';

        console.log('Cleared inputs');
      } else {
        statusMessage = "❌ Server error. Please try again.";
      }
    } catch (err) {
      statusMessage = "❌ Connection error. Is the backend running?";
      console.error(err);
    } finally {
      isSending = false;
      // Clear status message after 4 seconds
      setTimeout(() => {
        statusMessage = '';
      }, 4000);
    }
  }
</script>

<!-- Navbar -->
<nav class="fixed top-0 left-0 z-50 flex h-20 w-full items-center justify-between border-b border-white/10 bg-black/40 px-4 backdrop-blur-md sm:px-10">
    <a href="/" class="group flex items-center gap-2">
        <h1 class="text-xl font-black tracking-tighter text-white transition-colors group-hover:text-orange-500 sm:text-2xl sm:tracking-widest">
            ADWA <span class="text-orange-500 group-hover:text-white font-bold">AI</span>
        </h1>
    </a>
    <a href="/homepage">
        <button class="rounded-xl border border-white/20 bg-orange-500 px-6 py-2 text-sm font-bold uppercase tracking-wider text-white backdrop-blur-md transition-all hover:bg-white/10">
        homepage
        </button>
    </a>
</nav>

<main class="bg-zinc-950 text-white selection:bg-orange-500/30">

    <!-- Hero Section -->
    <section class="relative flex h-[80vh] w-full items-end justify-start overflow-hidden px-6 pb-20 sm:px-20">
        <img src="your-statue-image.jpg" alt="Adwa Victory" class="absolute inset-0 h-full w-full object-cover opacity-60 grayscale-[0.5]" />
        <div class="absolute inset-0 bg-gradient-to-t from-zinc-950 via-zinc-950/20 to-transparent"></div>
        <div class="relative z-10 max-w-4xl">
            <span class="mb-4 inline-block rounded-full border border-orange-500/50 bg-orange-500/10 px-4 py-1 text-xs font-bold uppercase tracking-widest text-orange-500">
                Est. 1896 · Digitalized 2026
            </span>
            <h2 class="mb-6 text-5xl font-black tracking-tight sm:text-7xl">
                Strategic <span class="text-orange-500">Intelligence.</span><br/>
                Historic Roots.
            </h2>
            <p class="max-w-xl text-lg text-zinc-400">
                Inspired by the victory of Adwa, we build AI solutions that empower sovereignty, celebrate heritage, and solve the world's most complex modern challenges.
            </p>
        </div>
    </section>

    <!-- Why Adwa -->
    <section class="border-t border-white/10 bg-zinc-900/50 px-6 py-24 sm:px-20">
        <div class="mx-auto flex max-w-6xl flex-col items-center gap-12 lg:flex-row">
            <div class="flex-1">
                <h2 class="mb-6 text-4xl font-bold">Why <span class="italic text-orange-500">Adwa?</span></h2>
                <div class="space-y-4 text-lg text-zinc-400">
                    <p>The Battle of Adwa wasn't just a military victory; it was a triumph of <strong>strategy over brute force</strong>.</p>
                    <p>At Adwa AI, we carry that torch into the digital frontier. We develop Large Language Models that prioritize <strong>African context</strong>.</p>
                </div>
            </div>
            <div class="w-full flex-1 rounded-xl bg-black p-6 font-mono text-sm text-green-500 shadow-2xl">
                <p class="text-zinc-600">// initializing_adwa_protocol.py</p>
                <p><span class="text-purple-400">import</span> intelligence</p>
                <p><span class="text-purple-400">def</span> <span class="text-blue-400">victory</span>(strategy, unity):</p>
                <p class="pl-4">year = <span class="text-orange-400">1896</span></p>
                <p class="pl-4">impact = strategy * unity</p>
                <p class="pl-4"><span class="text-purple-400">return</span> impact</p>
            </div>
        </div>
    </section>

    <!-- Builders Section -->
    <section class="px-6 py-24 sm:px-20 border-t border-white/5 bg-zinc-950">
        <div class="max-w-6xl mx-auto">
            <div class="mb-12">
                <h2 class="text-3xl font-bold mb-2 tracking-tight">The <span class="text-orange-500">Builders</span></h2>
                <p class="text-zinc-500 text-sm italic">Two minds, one mission.</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
                <div class="group border-l-2 border-zinc-800 pl-8 py-4 transition-all hover:border-orange-500">
                    <p class="text-[10px] uppercase tracking-[0.3em] text-orange-500 font-bold mb-2">Systems & AI Logic</p>
                    <h4 class="text-2xl font-bold text-white mb-1">Abel Alemu</h4>
                    <p class="text-zinc-400 text-sm leading-relaxed mb-6">Architecting the core engine and API integrations.</p>
                    <div class="flex gap-4">
                        <a href="https://github.com/RedShadow11754/" class="text-xs font-bold text-zinc-500 hover:text-white border border-zinc-800 px-3 py-1 rounded-md">GITHUB</a>
                        <a href="https://www.linkedin.com/in/abel-alemu-46044a3aa" class="text-xs font-bold text-zinc-500 hover:text-white border border-zinc-800 px-3 py-1 rounded-md">LINKEDIN</a>
                    </div>
                </div>
                <div class="group border-l-2 border-zinc-800 pl-8 py-4 transition-all hover:border-orange-500">
                    <p class="text-[10px] uppercase tracking-[0.3em] text-orange-500 font-bold mb-2">Interface & UX</p>
                    <h4 class="text-2xl font-bold text-white mb-1">Yordanos Bogale</h4>
                    <p class="text-zinc-400 text-sm leading-relaxed mb-6">Crafting the visual identity and user interaction flow.</p>
                    <div class="flex gap-4">
                        <a href="https://github.com/yorrr-pro" class="text-xs font-bold text-zinc-500 hover:text-white border border-zinc-800 px-3 py-1 rounded-md">GITHUB</a>
                        <a href="https://www.linkedin.com/in/yordanos-bogale-a67a07357/" class="text-xs font-bold text-zinc-500 hover:text-white border border-zinc-800 px-3 py-1 rounded-md">LINKEDIN</a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Feedback Section -->
    <section class="border-t border-white/5 bg-zinc-950 px-6 py-20 sm:px-20">
        <div class="mx-auto max-w-4xl rounded-2xl border border-white/5 bg-zinc-900/30 p-8 sm:p-12">
            <div class="mb-8 flex flex-col items-start gap-4 md:flex-row md:items-center md:justify-between">
                <div>
                    <h3 class="text-2xl font-bold text-white">Direct <span class="text-orange-500">Feedback</span></h3>
                    <p class="text-sm text-zinc-500">Have thoughts on the engine? Let the builders know.</p>
                </div>
                <div class="h-px w-full flex-1 bg-white/5 md:mx-8 md:block hidden"></div>
            </div>

            <!-- Form with manual refs for fallback clearing -->
            <form on:submit={sendFeedback} class="space-y-4">
                <div class="grid grid-cols-1 gap-4 sm:grid-cols-2">
                    <input
                        type="text"
                        placeholder="Name *"
                        bind:value={name}
                        bind:this={nameInput}
                        class="w-full rounded-lg border border-white/10 bg-black/50 px-4 py-3 text-sm text-white outline-none focus:border-orange-500/50 focus:ring-1 focus:ring-orange-500/50"
                    />
                    <input
                        type="email"
                        placeholder="Email (Optional)"
                        bind:value={email}
                        bind:this={emailInput}
                        class="w-full rounded-lg border border-white/10 bg-black/50 px-4 py-3 text-sm text-white outline-none focus:border-orange-500/50 focus:ring-1 focus:ring-orange-500/50"
                    />
                </div>
                <textarea
                    rows="4"
                    placeholder="Your message... *"
                    bind:value={feed}
                    bind:this={feedInput}
                    class="w-full rounded-lg border border-white/10 bg-black/50 px-4 py-3 text-sm text-white outline-none focus:border-orange-500/50 focus:ring-1 focus:ring-orange-500/50"
                ></textarea>

                <div class="flex flex-col items-end gap-2 sm:flex-row sm:items-center sm:justify-end sm:gap-4">
                    {#if statusMessage}
                        <span
                            class="text-sm font-medium {statusMessage.includes('❌') || statusMessage.includes('require')
                                ? 'text-red-400'
                                : 'text-green-500'}"
                        >
                            {statusMessage}
                        </span>
                    {/if}

                    <button
                        type="submit"
                        disabled={isSending}
                        class="group flex items-center gap-2 rounded-xl bg-orange-500 px-8 py-3 text-sm font-bold uppercase tracking-widest text-white transition-all hover:bg-orange-600 active:scale-95 disabled:opacity-50 disabled:cursor-not-allowed"
                    >
                        {isSending ? 'Sending...' : 'Send Message'}
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 transition-transform group-hover:translate-x-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
                        </svg>
                    </button>
                </div>
            </form>
        </div>
    </section>
</main>