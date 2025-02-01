import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers'
import ElementPlus from 'unplugin-element-plus/vite'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    // 按需定制主题配置
    ElementPlus({
      useSource: true,
    }),
    AutoImport({
      resolvers: [ElementPlusResolver({ importStyle: 'sass' })],
    }),
    Components({
      resolvers: [ElementPlusResolver({ importStyle: 'sass' })],
    }),
  ],
  // 预加载项目必需的组件
  optimizeDeps: {
    include: [
      "vue",
      "vue-router",
      "axios",
      "element-plus/es/components/base/style/css",
      "element-plus/es/components/message/style/css",
      "element-plus/es/components/message-box/style/css",
      "element-plus/es/components/form/style/css",
      "element-plus/es/components/form-item/style/css",
      "element-plus/es/components/button/style/css",
      "element-plus/es/components/input/style/css",
      "element-plus/es/components/input-number/style/css",
      "element-plus/es/components/switch/style/css",
      "element-plus/es/components/upload/style/css",
      "element-plus/es/components/menu/style/css",
      "element-plus/es/components/col/style/css",
      "element-plus/es/components/icon/style/css",
      "element-plus/es/components/row/style/css",
      "element-plus/es/components/tag/style/css",
      "element-plus/es/components/dialog/style/css",
      "element-plus/es/components/loading/style/css",
      "element-plus/es/components/radio/style/css",
      "element-plus/es/components/radio-group/style/css",
      "element-plus/es/components/popover/style/css",
      "element-plus/es/components/scrollbar/style/css",
      "element-plus/es/components/tooltip/style/css",
      "element-plus/es/components/dropdown/style/css",
      "element-plus/es/components/dropdown-menu/style/css",
      "element-plus/es/components/dropdown-item/style/css",
      "element-plus/es/components/sub-menu/style/css",
      "element-plus/es/components/menu-item/style/css",
      "element-plus/es/components/divider/style/css",
      "element-plus/es/components/card/style/css",
      "element-plus/es/components/link/style/css",
      "element-plus/es/components/breadcrumb/style/css",
      "element-plus/es/components/breadcrumb-item/style/css",
      "element-plus/es/components/table/style/css",
      "element-plus/es/components/tree-select/style/css",
      "element-plus/es/components/table-column/style/css",
      "element-plus/es/components/select/style/css",
      "element-plus/es/components/option/style/css",
      "element-plus/es/components/pagination/style/css",
      "element-plus/es/components/tree/style/css",
      "element-plus/es/components/alert/style/css",
      "element-plus/es/components/radio-button/style/css",
      "element-plus/es/components/checkbox-group/style/css",
      "element-plus/es/components/checkbox/style/css",
      "element-plus/es/components/tabs/style/css",
      "element-plus/es/components/tab-pane/style/css",
      "element-plus/es/components/rate/style/css",
      "element-plus/es/components/date-picker/style/css",
      "element-plus/es/components/notification/style/css",
      "element-plus/es/components/image/style/css",
      "element-plus/es/components/statistic/style/css",
      "element-plus/es/components/watermark/style/css",
      "element-plus/es/components/config-provider/style/css",
      "element-plus/es/components/text/style/css",
      "element-plus/es/components/drawer/style/css",
      "element-plus/es/components/color-picker/style/css",
    ],
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  css: {
    preprocessorOptions: {
      scss: {
        // 自动导入定制化样式文件进行样式覆盖
        additionalData: `
          @use "@/assets/css/index.scss" as *;
        `,
      }
    }
  },
})
