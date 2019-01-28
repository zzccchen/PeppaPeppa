<style scoped lang="less">
.index {
  width: 100%;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  text-align: center;
  h1 {
    height: 150px;
    img {
      height: 100%;
    }
  }
  h2 {
    color: #666;
    margin-bottom: 200px;
    p {
      margin: 0 0 50px;
    }
  }
  .ivu-row-flex {
    height: 100%;
  }
}
</style>
<template>
  <div style="text-align:center;background-image:url('https://cdn.bdstatic.com/login/bg-1920x1080.png@q_90');background-repeat:no-repeat; background-size:100% 100%;height:100vh;weight:100vw;">

    <header style="position:absolute;display:block;top:0;left:0;width:100%;height:60px;background-color:rgba(23, 23, 23, .35);z-index:1000;">
      <div style="width:1800px;height:100%;margin-right:auto;margin-left:auto;">
        <div style="float:left;margin-top:10px;font-size:26px;color:#fff;">PeppaPeppa</div>
        <div style="margin-top:18px;float:right;">
          <a href="https://github.com/zzccchen/PeppaPeppa"
            style="font-size:18px;color:#fff;">GitHub</a>
        </div>
      </div>
    </header>

    <Card style="width:847px;height:420px;margin:0 auto;position:relative;top:240px;border-radius:25px;"
      :padding=0>
      <tbody style="display:table-row-group;vertical-align:middle;">
        <tr style="display:table-row;vertical-align:inherit;">
          <td style="vertical-align:middle;text-align:center;width:472px;height:420px;border-right:1px solid #ececec;">
            <img src="https://s2.ax1x.com/2019/01/25/kmBWWt.jpg"
              style="width:80%;border-radius:50px">
          </td>
          <td style="display:table-cell;vertical-align:inherit;">
            <div style="width:373px;height:420px;position:relative;top:50px">
              <Tabs value="name1"
                style="margin:0 auto;width:300px;height:420vh">
                <TabPane label="密码登录"
                  name="name1">
                  <Input v-model="value1"
                    size="large"
                    style="top:6px;position:relative;"
                    placeholder="手机/邮箱/用户名" />
                  <Input v-model="value1"
                    size="large"
                    style="top:26px;position:relative;"
                    placeholder="密码" />
                  <input id="verify"
                    type="text"
                    value=""
                    style="top:46px;position:relative;width:150px;left:-75px;"
                    class="ivu-input ivu-input-large"
                    placeholder="验证码" />

                  <img id="code_img"
                    :src="img_url[randon_num()]"
                    style="top:18px;position:relative;width:150px;left:90px;"
                    @click="reload()">
                  <Button type="primary"
                    long
                    style="top:50px;position:relative;">登录</Button>
                </TabPane>
                <TabPane label="文件服务"
                  name="name2">
                  <Upload multiple
                    type="drag"
                    action="/api/ocr"
                    style="position:relative;top:7px;width:300px"
                    :on-success="handleSuccess">
                    <div style="padding: 20px 0">
                      <Icon type="ios-cloud-upload"
                        size="52"
                        style="color: #3399ff"></Icon>
                      <p>点击 或 拖拽 上传</p>
                    </div>

                  </Upload>
                </TabPane>
              </Tabs>
            </div>
          </td>
        </tr>
      </tbody>
    </Card>
  </div>
</template>
<script>
export default {
  data () {
    return {
      value1: null,
      value2: null,
      ocr_data: null,
      img_flag: 0,
      img_url: ["https://s2.ax1x.com/2019/01/26/knDrxx.png",
        "https://s2.ax1x.com/2019/01/26/knDIzt.png",
        "https://s2.ax1x.com/2019/01/26/knDLdg.png",
        "https://s2.ax1x.com/2019/01/26/knDjij.png",
        "https://s2.ax1x.com/2019/01/26/knDxWn.png",
        "https://s2.ax1x.com/2019/01/26/knrCLT.png",
        "https://s2.ax1x.com/2019/01/26/knrFwF.png",
        "https://s2.ax1x.com/2019/01/26/kn6tp9.png",
        "https://s2.ax1x.com/2019/01/26/kn6U61.png",
        "https://s2.ax1x.com/2019/01/26/kn600K.png"]
    }
  },
  methods: {
    reload () {
      this.$router.replace('/empty')
    },
    randon_num () {
      var num = Math.floor(Math.random() * 10);
      // console.log(num);
      return num;
    },
    handleSuccess (res, file, fileList) {
      var ocr_data = res.data.ocr_data;
      this.instance('success', ocr_data)
      // console.log(ocr_data)
    },
    instance (type, ocr_data) {
      const title = '识别成功';
      console.log(ocr_data)
      const content = '<h1>结果：' + ocr_data + '</h1>';
      switch (type) {
        case 'success':
          this.$Modal.success({
            title: title,
            content: content
          });
          break;
      }
    }
  }
}
</script>
