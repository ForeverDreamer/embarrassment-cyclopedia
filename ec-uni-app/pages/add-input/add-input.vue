<template>
	<view>
		<!-- 自定义导航栏 -->
		<uni-nav-bar status-bar="true" right-text="发布" left-icon="arrowleft" @click-left="back" @click-right="submit" >
			<view class="u-f-ajc nav-tab-bar" @tap="changeLook">
				<view>{{yinsi}}</view>
				<view class="icon iconfont icon-xialazhankai"></view>
			</view>
		</uni-nav-bar>
		<!-- 多行输入框 -->
		<view class="uni-textarea">
			<textarea v-model="text" placeholder="说一句话吧"/>
		</view>
		<!-- <view>文本框输入内容为：{{text}}</view> -->
		<!-- 上传多图 -->
		<upload-images @upload="onUpload"></upload-images>
		<!-- 弹出公告 -->
		<button @click="openPopup">打开弹出层</button>
		<uni-popup ref="popup" type="center" :mask-click="false">
			<view class="gonggao">
				<view class="u-f-ajc">
					<image src="../../static/common/add-input.png" mode="widthFix"></image>
				</view>
				<view>1.涉及黄色，政治，广告及骚扰信息</view>
				<view>1.涉及黄色，政治，广告及骚扰信息</view>
				<view>1.涉及黄色，政治，广告及骚扰信息</view>
				<view>1.涉及黄色，政治，广告及骚扰信息</view>
				<button type="default" @click="closePopup">朕知道了</button>
			</view>
		</uni-popup>
	</view>
</template>

<script>
	import uniNavBar from "../../components/uni-nav-bar/uni-nav-bar.vue"
	import uploadImages from "../../components/common/upload-images.vue"
	import uniPopup from "../../components/uni-popup/uni-popup.vue"
	
	let chgLook = ['所有人可见', '仅自己可见'];
	
	export default {
		components: {
			uniNavBar,
			uploadImages,
			uniPopup
		},
		data() {
			return {
				isGet: false,
				yinsi: "所有人可见",
				text: "",
				imgList: []
			}
		},
		onBackPress() {
			// 如果用户有编辑内容
			if (!this.text && this.imgList.length < 1) {
				return;
			}
			if (!this.isGet) {
				this.baocun();
				return true;
			}	
		},
		methods: {
			// 保存为草稿
			baocun() {
				uni.showModal({
					content: '是否要保存为草稿？',
					cancelText: '不保存',
					confirmText: '保存',
					success: res => {
						if (res.confirm) {
							console.log("保存")
						} else {
							console.log("不保存")
						}
						this.isGet = true;
						uni.navigateBack({
							delta: 1
						});
					}
				});
			},
			// 返回
			back() {
				uni.navigateBack({
					delta: 1
				});
			},
			// 发布
			submit() {
				console.log("发布")
			},
			// 隐私
			changeLook() {
				uni.showActionSheet({
				    itemList: chgLook,
				    success: (res) => {
				        this.yinsi = chgLook[res.tapIndex];
				    }
				});
			},
			// 上传图片
			onUpload(imgArr) {
				this.imgList = imgArr;
				console.log(this.imgList);
			},
			openPopup(){
			            this.$refs.popup.open()
			},
			closePopup(){
				this.$refs.popup.close()
			}
		}
	}
</script>

<style>
	.uni-textarea {
		border: 1rpx solid #EEEEEE;
	}
	.gonggao {
		width: 500rpx;
	}
	.gonggao image {
		width: 50%;
		margin-bottom: 20rpx;
	}
	.gonggao button {
		background: #FFE934;
		color: #171606;
	}
	.nav-tab-bar {
		width: 100%;
		margin-left: -25rpx;
	}
</style>
