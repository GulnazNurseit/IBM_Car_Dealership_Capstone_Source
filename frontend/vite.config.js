import { defineConfig } from 'vite';
export default defineConfig({server:{host:'0.0.0.0',proxy:{'/get_dealers/':{target:'http://django:8000',changeOrigin:true}}}});
