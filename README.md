<p>
<strong><h2>枕石の主页</h2></strong>
在大佬的<a href="https://github.com/imsyy/home">模板</a>上进行的修改，添加了微信的联系方式。
</p>

![枕石の主页](/screenshots/main.png)

### 手动部署
- 安装 node.js 环境
  - node > 16.16.0
  - npm > 8.15.0

- 然后以 **管理员权限** 运行 ```cmd``` 终端，并 ```cd``` 到 项目根目录

- 在 终端 中输入：
```
# 安装 pnpm
npm install -g pnpm

# 安装依赖
pnpm install

# 预览
pnpm dev

# 构建
pnpm build
```

构建完成后，静态资源会在 ```dist``` 目录 中生成，可将 dist 文件夹下的文件上传至服务器，也可使用 Vercel 等托管平台一键导入并自动部署

- 运行
```
# 使用 serve
npm install -g serve
serve dist
```