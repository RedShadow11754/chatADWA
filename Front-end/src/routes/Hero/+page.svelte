 <script> 
 import MenilikImg from "$lib/assets/heroes/Menelik.png"
 import TaytuImg from  "$lib/assets/heroes/Queen-Taitou.jpg"
 import AlulaImg from "$lib/assets/heroes/Alula.png"
 import BalchaImg from  "$lib/assets/heroes/balcha.png"
 import HabteImg from "$lib/assets/heroes/habte .png"
      // Svelte 5 Runes for State Manage ment
let heroes = $state([
  {
    id: 1,
    name: "Menelik II",
    title: "Emperor of Ethiopia",
    img: MenilikImg,
    short: "The victor of Adwa who preserved Ethiopia's sovereignty.",
    bio: `Emperor Menelik II (1844–1913) was one of the most influential rulers in Ethiopian history and the leader who secured Ethiopia’s independence during the era of European colonial expansion in Africa. Born Sahle Maryam, he became King of Shewa before ascending to the imperial throne in 1889. Menelik was a visionary statesman who worked to modernize Ethiopia while strengthening its unity. He expanded the empire’s territory, introduced modern infrastructure such as telegraph lines and roads, and promoted diplomatic relations with foreign powers.

His greatest legacy came during the conflict with Italy that led to the Battle of Adwa in 1896. When Italy attempted to impose the Treaty of Wuchale in a way that would make Ethiopia an Italian protectorate, Menelik rejected the interpretation and mobilized a massive national army composed of soldiers from many regions and ethnic groups. His leadership united the country in resistance to colonial rule. At the Battle of Adwa, Ethiopian forces decisively defeated the Italian army, making Ethiopia the only African nation to successfully resist European colonization during the Scramble for Africa. This victory became a symbol of African resistance and pride worldwide.`
  },

  {
    id: 2,
    name: "Empress Taytu Betul",
    title: "Empress & Strategist",
    img: TaytuImg,
    short: "Brilliant military advisor and commander of her own battalion.",
    bio: `Empress Taytu Betul (1851–1918) was one of the most powerful and influential women in Ethiopian history. Born into an aristocratic family with strong political connections, she became the wife and trusted advisor of Emperor Menelik II. Taytu was known for her intelligence, political awareness, and unwavering determination to defend Ethiopian sovereignty against foreign domination.

During the events leading to the Battle of Adwa, Taytu played a critical strategic role. She strongly opposed the Italian interpretation of the Treaty of Wuchale and urged resistance against any attempt to place Ethiopia under colonial control. Taytu organized and led her own contingent of soldiers and personally took part in the campaign. She is famously remembered for ordering Ethiopian forces to cut off the Italian water supply at the fortress of Mekelle, forcing the enemy into a difficult position.

Beyond the battlefield, Taytu was also a significant political figure in the imperial court and contributed to the founding and development of Addis Ababa as Ethiopia’s capital city. Her leadership, courage, and determination made her a symbol of national pride and one of the most respected women in Ethiopian history.`
  },

  {
    id: 3,
    name: "Ras Alula Engida",
    title: "The 'Abba Nega'",
    img: AlulaImg,
    short: "One of the greatest African generals of the 19th century.",
    bio: `Ras Alula Engida (1847–1897) was one of Ethiopia’s most brilliant military commanders and a key defender of the empire during the late nineteenth century. Rising from relatively modest origins, he gained prominence through his exceptional military skill, courage, and loyalty to Emperor Yohannes IV. Ras Alula quickly earned a reputation as a fearless general and a master strategist capable of leading troops in extremely difficult circumstances.

Throughout his career, Ras Alula commanded Ethiopian forces in numerous battles against foreign invaders and regional enemies. He played an important role in defending Ethiopia’s northern borders against Egyptian, Sudanese Mahdist, and Italian forces. His victories at battles such as Dogali demonstrated his tactical brilliance and his ability to inspire soldiers under his command.

Although Ras Alula died shortly after the Battle of Adwa, his legacy as one of Africa’s greatest military leaders remains strong. His leadership helped preserve Ethiopian independence during a time when most of Africa was falling under European colonial rule. He is remembered not only as a great warrior but also as a symbol of determination and resistance.`
  },

  {
    id: 4,
    name: "Fitawrari Habte Giyorgis",
    title: "Minister of War",
    img: HabteImg,
    short: "Renowned military strategist and advisor to the crown.",
    bio: `Fitawrari Habte Giyorgis Dinagde (1851–1927) was one of the most influential military leaders and statesmen of modern Ethiopian history. Originally born into humble circumstances, he rose through the ranks of the Ethiopian military through dedication, intelligence, and strong leadership ability. Over time he became one of Emperor Menelik II’s most trusted commanders and advisors.

Habte Giyorgis played an important role in organizing and strengthening the Ethiopian army during a critical period of national defense. His experience in military administration and battlefield leadership helped coordinate the diverse regional forces that formed the imperial army. During the campaigns that led to the Battle of Adwa, he served as a key commander helping to manage logistics, troop coordination, and strategic planning.

After the victory at Adwa, Habte Giyorgis continued to serve Ethiopia for many years, eventually becoming Minister of War and one of the most powerful officials in the imperial government. He contributed significantly to maintaining national stability and strengthening the Ethiopian state during the early twentieth century. His life represents dedication to service, discipline, and national unity.`
  },

  {
    id: 5,
    name: "Dejazmach Balcha Safo",
    title: "The Artillery Hero",
    img: BalchaImg,
    short: "Commanded the artillery units that devastated Italian lines.",
    bio: `Dejazmach Balcha Safo (1863–1936), often remembered by his nickname “Abba Nefso,” was a legendary Ethiopian military commander known for his bold personality, tactical intelligence, and fierce independence. Rising from relatively modest beginnings, Balcha Safo became one of the most respected officers in the Ethiopian imperial army during the reign of Emperor Menelik II.

During the Battle of Adwa, Balcha Safo commanded artillery forces that played a critical role in breaking Italian defensive positions. His leadership helped Ethiopian forces effectively deploy modern weapons captured or purchased from abroad. His courage and aggressive tactics contributed significantly to the overwhelming Ethiopian victory against the Italian army.

Balcha Safo continued to serve Ethiopia in various military and administrative roles after the victory at Adwa. Known for his strong character and determination, he remained an important regional leader and a defender of Ethiopian independence throughout his life. Today he is remembered as one of the brave commanders whose actions helped secure one of the most significant victories in African history.`
  }
]);


  let milestones = [
    { year: "1889", title: "Treaty of Wuchale", desc: "Signed between Ethiopia and Italy; the mistranslation led to war." },
    { year: "1895", title: "The Mobilization", desc: "Menelik II called 100,000 soldiers to defend the motherland." },
    { year: "Mar 1, 1896", title: "The Victory", desc: "Ethiopian forces crushed the Italian brigades in a single day." }
  ];

  let query = $state("");
  let selected = $state(null);

  // Svelte 5 Derived State (Replaces $: syntax)
  let filteredHeroes = $derived(
    heroes.filter(h => 
      h.name.toLowerCase().includes(query.toLowerCase().trim()) || 
      h.title.toLowerCase().includes(query.toLowerCase().trim())
    )
  );

  function openHero(h) { selected = h; }
  function closeHero() { selected = null; }

</script>

<!-- Navbar  -->
<nav class="fixed top-0 left-0 z-50 flex h-16 w-full items-center justify-between border-b border-white/10 bg-black/40 px-4 backdrop-blur-md sm:px-10">
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



<svelte:window onkeydown={(e) => e.key === "Escape" && closeHero()} />

<main class="min-h-screen bg-transparent text-gray-100 font-sans ">


  <section class="max-w-6xl mx-auto px-4 py-16 ">
    <header class="text-center mb-12">
      <h1 class="text-5xl md:text-7xl font-serif font-black text-transparent bg-clip-text bg-gradient-to-b from-white to-amber-200">
        ADWA: THE LEGACY
      </h1>
      <p class="mt-4 text-gray-100 max-w-xl mx-auto italic text-lg">"A victory that lit the torch for Pan-Africanism."</p>
      
      <div class="mt-8 flex justify-center">
        <input
          bind:value={query}
          placeholder="Search the defenders..."
          class="w-full max-w-md rounded-full px-6 py-3 bg-white/5 border border-white/10 focus:ring-2 focus:ring-amber-500 outline-none transition-all"
        />
      </div>
    </header>

    <div class="grid gap-6 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
      {#each filteredHeroes as hero (hero.id)}
        <article class="group bg-[#111] border border-white/5 rounded-2xl overflow-hidden hover:border-amber-500/40 transition-all duration-500">
          <div class="h-56 bg-black overflow-hidden">
            <img src={hero.img} alt={hero.name} class="w-full h-full object-cover opacity-70 group-hover:opacity-100 transition duration-700 grayscale group-hover:grayscale-0" />
          </div>
          <div class="p-6">
            <h3 class="text-2xl font-serif font-bold">{hero.name}</h3>
            <p class="text-amber-500 text-sm mb-4">{hero.title}</p>
            <button onclick={() => openHero(hero)} class="w-full py-2 bg-white/5 hover:bg-white text-white hover:text-black font-bold rounded-lg transition">
              Read Legacy
            </button>
          </div>
        </article>
      {/each}
    </div>
  </section>

  <section class="py-20 bg-black/40">
    <div class="max-w-4xl mx-auto px-6">
      <h2 class="text-center text-3xl font-serif font-bold mb-12 underline decoration-amber-500 underline-offset-8">TIMELINE</h2>
      <div class="relative border-l-2 border-white/10 ml-4 md:ml-0">
        {#each milestones as event}
          <div class="mb-10 ml-6 relative">
            <div class="absolute -left-[31px] top-1 w-4 h-4 bg-amber-500 rounded-full border-4 border-black"></div>
            <span class="text-amber-500 font-bold">{event.year}</span>
            <h4 class="text-xl font-bold text-white">{event.title}</h4>
            <p class="text-gray-400 text-sm mt-1">{event.desc}</p>
          </div>
        {/each}
      </div>
    </div>
  </section>

  {#if selected}
    <div class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-transparent backdrop-blur-sm" onclick={closeHero}>
      <aside class="relative max-w-2xl w-full bg-black p-8 rounded-3xl border border-white/10" onclick={(e) => e.stopPropagation()}>
        <div class="flex flex-col md:flex-row gap-6">
          <img src={selected.img} alt={selected.name} class="w-32 h-32 rounded-xl object-cover" />
          <div>
            <h3 class="text-3xl font-serif font-bold">{selected.name}</h3>
            <p class="text-amber-500 mb-4">{selected.title}</p>
            <p class="text-gray-300 leading-relaxed">{selected.bio}</p>
            <button onclick={closeHero} class="mt-6 px-6 py-2 bg-white/10 rounded-full hover:bg-white/20">Close</button>
          </div>
        </div>
      </aside>
    </div>
  {/if}
</main>

<style>
  @import url('https://fonts.googleapis.com');
  .font-serif { font-family: 'Playfair Display', serif; }
</style> 
