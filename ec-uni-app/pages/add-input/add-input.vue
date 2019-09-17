<template>
	<view>
		<!-- 自定义导航栏 -->
		<uni-nav-bar status-bar="true" right-text="发布" left-icon="arrowleft" @click-left="back" @click-right="submit" >
			<view class="u-f-ajc" @tap="changeLook">
				<view>所有人可见</view>
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
	</view>
</template>

<script>
	import uniNavBar from "../../components/uni-nav-bar/uni-nav-bar.vue"
	import uploadImages from "../../components/common/upload-images.vue"
	
	let chgLook = ['所有人可见', '仅自己可见'];
	
	export default {
		components: {
			uniNavBar,
			uploadImages
		},
		data() {
			return {
				yinsi: "所有人可见",
				text: "",
				imgList: []
			}
		},
		methods: {
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
						console.log(res.tapIndex);
				        this.yinsi = chgLook[res.tapIndex];
				    }
				});
			},
			// 上传图片
			onUpload(imgArr) {
				this.imgList = imgArr;
				console.log(this.imgList);
			}
		}
	}
</script>

<style>
	.uni-textarea {
		border: 1upx solid #EEEEEE;
	}
</style>
