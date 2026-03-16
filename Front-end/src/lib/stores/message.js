// messages.ts
import { writable } from 'svelte/store';

export type Msg = { role: 'user'|'assistant', content: string };
export const messages = writable<Msg[]>([]);

export const theme = writable<'dark'|'light'>(localStorage.getItem('theme') as any ?? 'dark');
theme.subscribe(v => localStorage.setItem('theme', v));