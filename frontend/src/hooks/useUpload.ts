export function useUpload() {
  async function uploadFile(file: File) {
    console.log("Upload placeholder:", file.name);
  }

  return { uploadFile };
}