<template>
  <!-- 社交链接 -->
  <div class="social">
    <div class="link">
      <a
        v-for="item in socialLinks"
        :key="item.name"
        :href="item.name === 'WeChat' ? null : item.url"
        target="_blank"
        @mouseenter="socialTip = item.tip"
        @mouseleave="socialTip = '通过这里联系我吧'"
        @click="handleClick(item)"
      >
        <img class="icon" :src="item.icon" height="24" />
      </a>
    </div>
    <span class="tip">{{ socialTip }}</span>
  </div>

  <!-- 微信弹窗 -->
  <div v-if="showWeChatPopup" class="wechat-popup">
      <img
        class="wechat-image"
        :src="socialLinks.find(item => item.name === 'WeChat').url"
        :style="{ width: weChatPopupWidth, height: weChatPopupHeight }"
      />
      <button class="close-button" @click="closePopup">
        <Icon size="24">
          <TimesCircleRegular />
        </Icon>
      </button>
  </div>
</template>

<script setup>
import { Icon } from "@vicons/utils";
import { TimesCircleRegular} from "@vicons/fa"; //

import socialLinks from "@/assets/socialLinks.json";

// 社交链接提示
const socialTip = ref("通过这里联系我吧");

// 微信弹窗相关数据
const showWeChatPopup = ref(false);
const weChatPopupWidth = ref('190px'); // 适当调整宽度
const weChatPopupHeight = ref('259px'); // 适当调整高度

// 处理点击事件的函数
const handleClick = (item) => {
  if (item.name === 'WeChat') {
    // socialTip.value = "扫码添加好友~";
    showWeChatPopup.value = true;
  }
};

// 关闭弹窗
const closePopup = () => {
  showWeChatPopup.value = false;
};

</script>

<style lang="scss" scoped>

.wechat-popup {
  position: fixed;
  top: 50%;
  left: 40%;
  transform: translate(-50%, -50%);
  background-color: #fff;
  border-radius: 10px;
}

.wechat-image {
  width: 100%;
  height: 100%;
  border-radius: 10px;
}

.close-button {
  position: absolute;
  top: 10px;
  right: 10px;
  cursor: pointer;
  background: none;
  border: none;
  font-size: 20px;
  color: #000;
  outline: none;
}

.close-button:hover {
  color: #ff0000; /* 鼠标悬停时的颜色 */
}

.social {
  margin-top: 1rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  max-width: 460px;
  width: 100%;
  height: 42px;
  background-color: transparent;
  border-radius: 6px;
  backdrop-filter: blur(0);
  animation: fade 0.5s;
  transition:
    background-color 0.3s,
    backdrop-filter 0.3s;
  @media (max-width: 840px) {
    max-width: 100%;
    justify-content: center;
    .link {
      justify-content: space-evenly !important;
      width: 90%;
    }
    .tip {
      display: none !important;
    }
  }

  .link {
    display: flex;
    align-items: center;
    justify-content: center;
    a {
      display: inherit;
      .icon {
        margin: 0 12px;
        transition: transform 0.3s;
        &:hover {
          transform: scale(1.1);
        }
        &:active {
          transform: scale(1);
        }
      }
    }
  }
  .tip {
    display: none;
    margin-right: 12px;
    animation: fade 0.5s;
  }
  @media (min-width: 768px) {
    &:hover {
      background-color: #00000040;
      backdrop-filter: blur(5px);
      .tip {
        display: block;
      }
    }
  }
}
</style>
