<script>
    import { tick } from 'svelte';

    // Svelte 5 Runes for reactivity
    let messages = $state([
        {
            role: "assistant",
            content: "Selam! I am Adwa AI. Ask me anything about the Battle of Adwa and the people behind Ethiopia’s historic victory."
        }
    ]);
    let input = $state("");
    let isTyping = $state(false);

    // Auto-scroll effect
    $effect(() => {
        messages.length; // Dependency: runs when message count changes
        const container = document.querySelector('.custom-scrollbar');
        if (container) {
            // tick() ensures Svelte has finished rendering the new bubble before scrolling
            tick().then(() => {
                container.scrollTo({ top: container.scrollHeight, behavior: 'smooth' });
            });
        }
    });

    async function sendMessage() {
        if (!input.trim() || isTyping) return;

        const question = input;
        messages.push({ role: "user", content: question });
        input = "";
        isTyping = true;

        try {
            // --- REPLACE THIS WITH YOUR FETCH CALL LATER ---
            await new Promise((resolve) => setTimeout(resolve, 1500));
            const answer = " The Battle of Adwa was fought in 1896 between Ethiopia and Italy. Ethiopian forces led by Emperor Menelik II defeated the Italian army.";
            
            messages.push({ role: "assistant", content: answer });
        } catch (error) {
            messages.push({ role: "assistant", content: "⚠️ Something went wrong." });
        } finally {
            isTyping = false;
        }
    }
</script>



<div class="flex flex-col h-[600px] w-full max-w-4xl mx-auto mt-10 rounded-3xl border border-white/10 bg-black/5 backdrop-blur-2xl shadow-2xl overflow-hidden text-xl">
    
    <!-- 1. Message Display Area -->
    <div class="flex-1 overflow-y-auto p-6 space-y-4 custom-scrollbar">
        {#each messages as msg}
            {#if msg.role === "assistant"}
                <div class="flex justify-start">
                    <div class="max-w-[80%] rounded-2xl rounded-tl-none bg-black/20 p-4 text-white border border-white/5">
                        <p class="text-sm font-bold text-orange-400 mb-1">Adwa AI</p>
                        <p class="break-words whitespace-pre-wrap">{msg.content}</p>
                    </div>
                </div>
            {:else}
                <div class="flex justify-end">
                    <div class="max-w-[80%] rounded-2xl rounded-tr-none bg-orange-600 p-4 text-white shadow-lg">
                        <p class="break-words whitespace-pre-wrap">{msg.content}</p>
                    </div>
                </div>
            {/if}
        {/each}

        <!-- FIX: isTyping MUST be outside the #each loop -->
        {#if isTyping}
            <div class="flex justify-start">
                <div class="bg-white/10 p-4 rounded-2xl rounded-tl-none border border-white/5">
                    <div class="flex gap-1">
                        <div class="w-2 h-2 bg-orange-400 rounded-full animate-bounce"></div>
                        <div class="w-2 h-2 bg-orange-400 rounded-full animate-bounce [animation-delay:0.2s]"></div>
                        <div class="w-2 h-2 bg-orange-400 rounded-full animate-bounce [animation-delay:0.4s]"></div>
                    </div>
                </div>
            </div>
        {/if}
    </div>

    <!-- 2. Input Box Area -->
    <div class="p-4 bg-black/20 border-t border-white/10">
        <div class="relative flex items-center">
            <input 
                type="text" 
                placeholder="Ask Adwa AI anything..." 
                bind:value={input}
                onkeydown={(e) => e.key === "Enter" && sendMessage()}
                class="w-full bg-white/5 border border-white/10 rounded-2xl py-4 pl-6 pr-16 text-white placeholder:text-gray-400 focus:outline-none focus:ring-2 focus:ring-orange-500/50 transition-all"
            />

            <button
                onclick={sendMessage}
                class="absolute right-2 p-2 bg-orange-600 hover:bg-orange-500 text-white rounded-xl transition-all active:scale-95"
            >
                <!-- Send Icon -->
                <svg xmlns="http://www.w3.org" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
            </button>
        </div>
        <p class="text-[10px] text-center text-gray-500 mt-2 italic">
            Adwa AI can make mistakes. Check important info.
        </p>
    </div>
</div>

<style>
    .custom-scrollbar::-webkit-scrollbar { width: 6px; }
    .custom-scrollbar::-webkit-scrollbar-thumb {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
    }
</style>


















































<!-- <script>
    import { tick } from 'svelte';
    // In Svelte 5, you MUST use $state for variables to update the UI
    let messages = $state([
        {
            role: "assistant",
            content: "Selam! I am the Adwa AI assistant. How can I help you explore our history today?"
        }
    ]);

        // This runs every time the messages array changes
    $effect(() => {
        messages; // Dependency
        const container = document.querySelector('.custom-scrollbar');
        if (container) {
            container.scrollTo({ top: container.scrollHeight, behavior: 'smooth' });
        }
    });

    let input = $state("");

    async function sendMessage() {
        console.log("sendMessage triggered");

        if (!input.trim()) return;

        const question = input;
        
        // Push the user message
        messages.push({ role: "user", content: question });

        // Clear the input immediately
        input = "";

        try {
            // Simulated delay
            await new Promise((resolve) => setTimeout(resolve, 1000));

            const answer = "The Battle of Adwa was fought in 1896 between Ethiopia and Italy. Ethiopian forces led by Emperor Menelik II defeated the Italian army.";

            // Push the assistant message
            messages.push({ role: "assistant", content: answer });
            
        } catch (error) {
            messages.push({ role: "assistant", content: "⚠️ Something went wrong." });
        }
    }


//with actual backend

//     <script>
//     let messages = $state([{ role: "assistant", content: "Selam! I am the Adwa AI assistant..." }]);
//     let input = $state("");
//     let isTyping = $state(false); // New: Track if the bot is thinking

//     async function sendMessage() {
//         if (!input.trim() || isTyping) return;

//         const question = input;
//         messages.push({ role: "user", content: question });
//         input = "";
//         isTyping = true; // Show loading state

//         try {
//             // THE REAL API CALL
//             const response = await fetch('/api/chat', { // Your backend URL
//                 method: 'POST',
//                 headers: { 'Content-Type': 'application/json' },
//                 body: JSON.stringify({ prompt: question })
//             });

//             if (!response.ok) throw new Error('Network error');

//             const data = await response.json();
            
//             // Push the actual answer from your backend
//             messages.push({ role: "assistant", content: data.answer });
            
//         } catch (error) {
//             messages.push({ role: "assistant", content: "⚠️ Sorry, I'm having trouble connecting right now." });
//         } finally {
//             isTyping = false; // Hide loading state
//         }
//     }
// </script>


</script>
 -->








<!-- 

<div class="flex flex-col h-[600px] w-full max-w-4xl mx-auto mt-10 rounded-3xl border border-white/10 bg-white/5 backdrop-blur-2xl shadow-2xl overflow-hidden">
    
   1. Message Display Area (Scrollable) 
    <div class="flex-1 overflow-y-auto p-6 space-y-4 custom-scrollbar">

        {#each messages as msg, i (i)}

            {#if msg.role === "assistant"}
                <div class="flex justify-start">
                    <div class="max-w-[80%] rounded-2xl rounded-tl-none bg-white/10 p-4 text-white border border-white/5">
                        <p class="text-sm font-bold text-orange-400 mb-1">Adwa AI</p>
                        <p>{msg.content}</p>
                    </div>
                </div>
            {:else}
                <div class="flex justify-end">
                    <div class="max-w-[80%] rounded-2xl rounded-tr-none bg-orange-600 p-4 text-white shadow-lg">
                        <p>{msg.content}</p>
                    </div>
                </div>
            {/if}

            {#if isTyping}
                <div class="flex justify-start">
                    <div class="bg-white/10 p-4 rounded-2xl rounded-tl-none border border-white/5">
                        <div class="flex gap-1">
                            <div class="w-2 h-2 bg-orange-400 rounded-full animate-bounce"></div>
                            <div class="w-2 h-2 bg-orange-400 rounded-full animate-bounce [animation-delay:0.2s]"></div>
                            <div class="w-2 h-2 bg-orange-400 rounded-full animate-bounce [animation-delay:0.4s]"></div>
                        </div>
                    </div>
                </div>
            {/if}


        {/each}

    </div>


    <div class="p-4 bg-black/20 border-t border-white/10">


        <input 
            type="text" 
            placeholder="Ask Adwa AI anything..." 
            bind:value={input}
            onkeydown={(e) => {
                if (e.key === "Enter") {
                    e.preventDefault();
                    sendMessage();
                }
            }}
            class="w-full bg-white/5 border border-white/10 rounded-2xl py-4 pl-6 pr-16 text-white
             placeholder:text-gray-400 focus:outline-none focus:ring-2 focus:ring-orange-500/50 transition-all"
             />

        <button
            onclick={sendMessage}
            class="absolute right-2 p-2 bg-orange-600 hover:bg-orange-500 text-white rounded-xl transition-all active:scale-95"
        >
            send
        </button>


    </div>
        <p class="text-[10px] text-center text-gray-500 mt-2 italic">
            Adwa AI can make mistakes. Check important info.
        </p>
</div> -->



<!-- <style>
    /* Makes the scrollbar look clean like the rest of the UI */
    .custom-scrollbar::-webkit-scrollbar {
        width: 6px;
    }
    .custom-scrollbar::-webkit-scrollbar-thumb {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
    }
</style> -->


