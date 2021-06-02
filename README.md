# MydailyFudan

平安复旦自动化提交


## 如何使用
1. Fork 本代码库
![image](https://user-images.githubusercontent.com/55427967/120477122-ffb25c80-c3dd-11eb-9530-b6d65c866ffe.png)
3. 配置 Secret  
   在 Settings - Secret 页面添加如下内容：
   - USERNAME: 学号
   - PASSWORD: UIS密码
![image](https://user-images.githubusercontent.com/55427967/120477728-b0b8f700-c3de-11eb-9bf1-f5d1f8daca3d.png)
3. 修改[main.yml](./.github/workflow/main.yml)中的`cron`为你喜欢的打卡时间(注为UTC时间，相对北京时间慢8小时),依次为分 时 周 月 年，30 8 * * *表示每天八点半提交 。GitHub Actions运行会有15分钟以内的延迟。
![image](https://user-images.githubusercontent.com/55427967/120478357-59ffed00-c3df-11eb-85da-bbb09ad57d45.png)

4. 开启 Workflow  
   在 Actions 页面：
   - 开启 Workflows
   - 选择 `Fudan Daily` workflow, enable workflow
![image](https://user-images.githubusercontent.com/55427967/120477522-70597900-c3de-11eb-9e7c-8068191f3639.png)

## 声明
本代码参考自Wendy1021/fudanDaily。
